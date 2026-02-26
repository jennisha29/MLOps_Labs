# Lab_03 — Docker

---

## 1. Prerequisites

Docker Desktop must be installed and running.
Download from: `https://www.docker.com/get-started`

Check it is working:

```bash
docker --version
```

---

## 2. Navigate into Lab_03

```bash
cd Lab_03
```

---

## 3. Build the Docker Image

```bash
docker build -t lab3:v1 .
```

Takes ~20–40 seconds the first time. Faster on repeat builds (Docker caches layers).

---

## 4. Save the Image as a TAR File

```bash
docker save lab3:v1 > my_image.tar
```

Exports the full image (~126MB) to a portable file. Verify:

```bash
ls -lh my_image.tar
```

---

## 5. Test the TAR File

Proves the TAR is a complete, self-contained export:

```bash
docker rmi -f lab3:v1
docker load < my_image.tar
# Output: Loaded image: lab3:v1
```

---

## 6. Run the Tests

```bash
docker run --rm lab3:v1 pytest -q
```

Expected:

```
............                    [100%]
12 passed in ~19s
```

---

## 7. Train the Model

```bash
docker run --rm -v "$PWD/data:/app/data" lab3:v1
```

Expected:

```
The model training was successful
```

The `-v` flag saves outputs from inside the container to your local `data/` folder.
Without it, files would be lost when the container stops.

---

## 8. Verify Outputs

```bash
ls -la data/
```

You should see:

```
california_gbr_model.pkl    ← trained model
metrics.json                ← MSE + R² scores
feature_importance.json     ← feature importances sorted descending
```

Check metrics:

```bash
cat data/metrics.json
```

Expected:

```json
{
  "dataset": "california_housing",
  "model": "GradientBoostingRegressor",
  "mse": 0.2939973248643864,
  "r2": 0.7756446042829697,
  "train_rows": 16512,
  "test_rows": 4128,
  "features": 8
}
```

Check feature importances:

```bash
cat data/feature_importance.json
```

Expected (sorted descending):

```json
[
  { "feature": "MedInc",     "importance": 0.604258 },
  { "feature": "AveOccup",   "importance": 0.122835 },
  { "feature": "Longitude",  "importance": 0.109852 },
  ...
]
```

---

## 9. Open the Dashboard

```bash
python3 -m http.server 8000
```

Then open: `http://localhost:8000/dashboard/dashboard.html`

---

## Common Commands

```bash
cd Lab_03
docker build -t lab3:v1 .
docker save lab3:v1 > my_image.tar
docker rmi -f lab3:v1
docker load < my_image.tar
docker run --rm lab3:v1 pytest -q
docker run --rm -v "$PWD/data:/app/data" lab3:v1
cat data/metrics.json
cat data/feature_importance.json
python3 -m http.server 8000
```

---
