from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json
from pathlib import Path

def main():
    out_dir = Path("data")
    out_dir.mkdir(parents=True, exist_ok=True)

    # dataset
    ds = fetch_california_housing()
    X, y = ds.data, ds.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    metrics = {
        "dataset": "california_housing",
        "model": "GradientBoostingRegressor",
        "mse": mse,
        "r2": r2,
        "train_rows": len(X_train),
        "test_rows": len(X_test),
        "features": X.shape[1],
    }

    importances = model.feature_importances_.tolist()
    feature_importance = sorted(
        [{"feature": name, "importance": float(val)} for name, val in zip(ds.feature_names, importances)],
        key=lambda x: x["importance"],
        reverse=True,
    )
    with open(out_dir / "feature_importance.json", "w") as f:
        json.dump(feature_importance, f, indent=2)

    joblib.dump(model, out_dir / "california_gbr_model.pkl")
    with open(out_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("The model training was successful")

if __name__ == "__main__":
    main()
