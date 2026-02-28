# Lab03_Flask

---

## 1. Prerequisites

Docker Desktop must be installed and running.
Download from: `https://www.docker.com/get-started`

Check if it is working:

```bash
docker --version
```

---

## 2. Navigate into Lab03_Flask

```bash
cd Lab_03/Lab03_Flask
```

---

## 3. Start the App

```bash
docker compose up
```

Two things happen in order:

- **ml_trainer** trains the neural network and saves the model and scaler to a shared volume
- **ml_serving** picks them up and starts the Flask server

Training takes a few minutes — you'll see epoch logs scrolling in the terminal.

Once you see this, the app is ready:

```
ml_serving  |  * Running on all addresses (0.0.0.0)
ml_serving  |  * Running on http://127.0.0.1:5000
```

---

## 4. Open the App

```
http://localhost:5001
```

---

## 5. Test a Prediction

Enter these values and click **ANALYZE**:

**Setosa**
| Field | Value |
|-------|-------|
| Sepal Length | `5.1` |
| Sepal Width | `3.5` |
| Petal Length | `1.4` |
| Petal Width | `0.2` |

Expected: `SETOSA` — CONFIDENCE: ~99.74%

**Versicolor**
| Field | Value |
|-------|-------|
| Sepal Length | `6.0` |
| Sepal Width | `2.9` |
| Petal Length | `4.5` |
| Petal Width | `1.5` |

Expected: `VERSICOLOR` — CONFIDENCE: ~91.95%

**Virginica**
| Field | Value |
|-------|-------|
| Sepal Length | `6.7` |
| Sepal Width | `3.1` |
| Petal Length | `5.6` |
| Petal Width | `2.4` |

Expected: `VIRGINICA` — CONFIDENCE: ~99.71%

---

## 6. Test the Health Endpoint

```bash
curl http://localhost:5001/health
```

Expected:

```json
{ "model": "iris_classifier", "status": "ok" }
```

---

## 7. Stop the App

```bash
docker compose down
```

---

## Common Commands

```bash
cd Lab_03/Lab03_Flask

# start
docker compose up

# start in background
docker compose up -d

# view logs
docker compose logs -f

# stop
docker compose down

# rebuild from scratch after code changes
docker compose up --build
```

---

> **Note:** Make sure these 3 images are inside `src/statics/` before running:
> `setosa.jpeg`, `versicolor.jpeg`, `virginica.jpeg`
