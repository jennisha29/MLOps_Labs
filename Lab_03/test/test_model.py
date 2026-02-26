import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error

def test_dataset_structure():
    ds = fetch_california_housing()
    assert hasattr(ds, "data")
    assert hasattr(ds, "target")
    assert hasattr(ds, "feature_names")
    assert ds.data.shape[1] == 8
    assert len(ds.feature_names) == 8
    assert ds.data.shape[0] > 10000
    assert ds.target.shape[0] == ds.data.shape[0]

def test_dataset_has_no_missing_values():
    ds = fetch_california_housing()
    assert np.isfinite(ds.data).all()
    assert np.isfinite(ds.target).all()

def test_dataset_feature_names():
    ds = fetch_california_housing()
    expected = {"MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"}
    assert set(ds.feature_names) == expected

# split test

def test_split_sizes():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    n = ds.data.shape[0]
    assert X_train.shape[0] + X_test.shape[0] == n
    assert y_train.shape[0] + y_test.shape[0] == n
    assert abs(X_test.shape[0] - int(0.2 * n)) <= 2
    assert abs(X_train.shape[0] - int(0.8 * n)) <= 2

def test_split_is_reproducible():
    ds = fetch_california_housing()
    X_train1, X_test1, y_train1, y_test1 = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    X_train2, X_test2, y_train2, y_test2 = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    assert np.array_equal(X_train1, X_train2)
    assert np.array_equal(X_test1, X_test2)
    assert np.array_equal(y_train1, y_train2)
    assert np.array_equal(y_test1, y_test2)

# testing model

def test_model_trains():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    assert hasattr(model, "estimators_")
    assert model.estimators_ is not None

def test_prediction_shape():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    assert preds.shape == y_test.shape

def test_predictions_are_valid():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    assert np.isfinite(preds).all()
    assert preds.min() > -1.0
    assert preds.max() < 7.0

# testing metrics

def test_r2_score():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    r2 = r2_score(y_test, model.predict(X_test))
    assert r2 > 0.4

def test_mse_score():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    mse = mean_squared_error(y_test, model.predict(X_test))
    assert mse > 0
    assert mse < 5.0

def test_model_is_deterministic():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )
    model1 = GradientBoostingRegressor(random_state=42)
    model1.fit(X_train, y_train)
    r2_1 = r2_score(y_test, model1.predict(X_test))

    model2 = GradientBoostingRegressor(random_state=42)
    model2.fit(X_train, y_train)
    r2_2 = r2_score(y_test, model2.predict(X_test))

    assert abs(r2_1 - r2_2) < 1e-12

def test_feature_importances_length():
    ds = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42
    )

    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)

    assert hasattr(model, "feature_importances_")
    assert len(model.feature_importances_) == 8
    assert np.isfinite(model.feature_importances_).all()
    assert model.feature_importances_.sum() > 0
