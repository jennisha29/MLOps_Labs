import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import pickle
import os
import base64

def load_data():
    """
    Loads data from a CSV file, serializes it, and returns the serialized data.
    Returns:
        str: Base64-encoded serialized data (JSON-safe).
    """
    print("Loading E-Commerce Customers dataset...")
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/ecommerce_customers.csv"))
    print(f"Loaded {len(df)} rows with columns: {list(df.columns)}")

    serialized_data = pickle.dumps(df)
    return base64.b64encode(serialized_data).decode("ascii")

def data_preprocessing(data_b64: str):
    """
    Deserializes base64-encoded pickled data, performs preprocessing,
    and returns base64-encoded pickled payload containing:
      - X_scaled
      - scaler
      - feature_cols
    """
    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)

    df = df.dropna()

    feature_cols = ["TOTAL_SPEND", "BROWSE_SESSIONS", "LOYALTY_POINTS"]
    missing = [c for c in feature_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in ecommerce_customers.csv: {missing}")

    X = df[feature_cols].astype(float)

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    payload = {"X_scaled": X_scaled, "scaler": scaler, "feature_cols": feature_cols}

    payload_serialized = pickle.dumps(payload)
    return base64.b64encode(payload_serialized).decode("ascii")

def build_save_model(payload_b64: str, filename: str):
    """
    Trains KMeans for k=1..50 to compute SSE, finds optimal k via elbow,
    trains final KMeans(best_k), saves model+scaler+metadata.
    Returns:
        str: Base64-encoded pickled dict with ks/sse/best_k (JSON-safe).
    """

    data_bytes = base64.b64decode(payload_b64)
    payload = pickle.loads(data_bytes)

    X_scaled = payload["X_scaled"]
    scaler = payload["scaler"]
    feature_cols = payload["feature_cols"]

    kmeans_kwargs = {"init": "k-means++", "n_init": 10, "max_iter": 300, "random_state": 42}

    ks = list(range(1, 51))
    sse = []
    for k in ks:
        km = KMeans(n_clusters=k, **kmeans_kwargs)
        km.fit(X_scaled)
        sse.append(float(km.inertia_))

    kl = KneeLocator(ks, sse, curve="convex", direction="decreasing")
    best_k = int(kl.elbow) if kl.elbow is not None else 3
    print(f"Optimal no. of clusters (elbow): {best_k}")

    final_model = KMeans(n_clusters=best_k, **kmeans_kwargs)
    final_model.fit(X_scaled)

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "wb") as f:
        pickle.dump(
            {
                "model": final_model,
                "scaler": scaler,
                "feature_cols": feature_cols,
                "best_k": best_k,
                "ks": ks,
                "sse": sse,
            },
            f,
        )
    print(f"Saved model bundle to: {output_path}")

    info_serialized = pickle.dumps({"best_k": best_k, "ks": ks, "sse": sse})
    return base64.b64encode(info_serialized).decode("ascii")


def load_model_elbow(filename: str, sse_info_b64: str):
    """
    Loads the saved model bundle, predicts clusters for test_ecommerce.csv
    after scaling using training scaler.
    Returns:
        str: Base64-encoded pickled dict (best_k + predictions + ks/sse) (JSON-safe).
    """

    model_path = os.path.join(os.path.dirname(__file__), "../model", filename)
    with open(model_path, "rb") as f:
        bundle = pickle.load(f)

    model = bundle["model"]
    scaler = bundle["scaler"]
    feature_cols = bundle["feature_cols"]
    best_k = int(bundle["best_k"])

    sse_info_bytes = base64.b64decode(sse_info_b64)
    sse_info = pickle.loads(sse_info_bytes)
    ks = sse_info["ks"]
    sse = sse_info["sse"]

    test_path = os.path.join(os.path.dirname(__file__), "../data/test_ecommerce.csv")
    test_df = pd.read_csv(test_path).dropna()

    missing = [c for c in feature_cols if c not in test_df.columns]
    if missing:
        raise ValueError(f"Missing required columns in test_ecommerce.csv: {missing}")

    X_test = test_df[feature_cols].astype(float)
    X_test_scaled = scaler.transform(X_test)

    preds = model.predict(X_test_scaled).tolist()
    preds = [int(p) for p in preds]

    result = {"best_k": best_k, "predictions": preds, "ks": ks, "sse": sse}
    print(f"Predicted {len(preds)} rows using best_k={best_k}")

    result_serialized = pickle.dumps(result)
    return base64.b64encode(result_serialized).decode("ascii")

def generate_visualizations(result_b64: str):
    """
    Generates and saves:
      1) elbow_curve.png  (SSE vs k, highlight best_k)
      2) cluster_scatter.png (TOTAL_SPEND vs BROWSE_SESSIONS colored by cluster)

    Returns:
        dict: JSON-safe dict with output paths.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    result_bytes = base64.b64decode(result_b64)
    result = pickle.loads(result_bytes)

    best_k = result["best_k"]
    ks = result["ks"]
    sse = result["sse"]

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "working_data")
    os.makedirs(output_dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ks, sse, marker="o", linewidth=2, markersize=4, label="SSE")
    ax.axvline(best_k, linestyle="--", linewidth=2, label=f"Selected k={best_k}")
    ax.set_title("Elbow Method — SSE vs Number of Clusters (k)")
    ax.set_xlabel("k")
    ax.set_ylabel("SSE (Inertia)")
    ax.grid(True, alpha=0.3)
    ax.legend()

    elbow_path = os.path.join(output_dir, "elbow_curve.png")
    fig.savefig(elbow_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved elbow curve: {elbow_path}")

    model_path = os.path.join(os.path.dirname(__file__), "../model", "model.sav")
    with open(model_path, "rb") as f:
        bundle = pickle.load(f)

    model = bundle["model"]
    scaler = bundle["scaler"]
    feature_cols = bundle["feature_cols"]

    data_path = os.path.join(os.path.dirname(__file__), "../data/ecommerce_customers.csv")
    df = pd.read_csv(data_path).dropna()

    X = df[feature_cols].astype(float)
    X_scaled = scaler.transform(X)
    labels = model.predict(X_scaled)

    fig, ax = plt.subplots(figsize=(10, 7))
    sc = ax.scatter(
        df["TOTAL_SPEND"],
        df["BROWSE_SESSIONS"],
        c=labels,
        s=15,
        alpha=0.7,
    )
    ax.set_title(f"E-Commerce Customer Segments (k={best_k})")
    ax.set_xlabel("TOTAL_SPEND")
    ax.set_ylabel("BROWSE_SESSIONS")
    ax.grid(True, alpha=0.3)
    plt.colorbar(sc, ax=ax, label="Cluster")

    scatter_path = os.path.join(output_dir, "cluster_scatter.png")
    fig.savefig(scatter_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved scatter plot: {scatter_path}")

    return {"elbow_curve": elbow_path, "cluster_scatter": scatter_path}