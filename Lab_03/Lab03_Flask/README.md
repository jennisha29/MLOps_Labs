# Lab03_Flask — Flask + TensorFlow

Training a neural network on the Iris dataset and deploying it as a web app using Flask and Docker Compose. Enter the flower measurements in the browser and get the predicted species with a confidence score.

---

## Overview

1. **Training** a neural network on the Iris dataset (`model_training.py`)
2. **Saving** the trained model (`my_model.keras`) and input scaler (`scaler.pkl`) to a shared Docker volume
3. **Serving** predictions via a Flask API (`main.py`)
4. **Showing** results in a browser — predicted species, confidence %, and a flower image

## Features

- **Model architecture** — added a hidden layer, BatchNormalization, and Dropout(0.2) to prevent overfitting.
- **Early stopping** — training stops automatically when validation loss stops improving.
- **Scaler saved** — the StandardScaler is saved as `scaler.pkl` and loaded in the serving container.
- **Confidence score** — the API returns the model's confidence % and the predicted class.
- **Health endpoint** — added `/health` to confirm the model and server are running.
- **Port** — changed from 4000/80 to 5000 (container) → 5001 (host).

---

## Project Structure

```
Lab03_Flask/
├── src/
│   ├── main.py               # Flask app — serves predictions
│   ├── model_training.py     # Trains and saves model + scaler
│   ├── templates/
│   │   └── predict.html      # Browser UI
│   └── statics/              # Flower images
│       ├── setosa.jpeg
│       ├── versicolor.jpeg
│       └── virginica.jpeg
├── Dockerfile                # Multi-stage build
├── docker-compose.yml        # Two services: trainer + server
├── requirements.txt
└── README.md
```

---

## Results

| Species    | Confidence |
| ---------- | ---------- |
| Setosa     | 99.74%     |
| Versicolor | 91.95%     |
| Virginica  | 99.71%     |

Test Accuracy: **100%** on the Iris test set.

---

## Endpoints

| Endpoint   | Method | What it does                           |
| ---------- | ------ | -------------------------------------- |
| `/`        | GET    | Loads the prediction UI                |
| `/predict` | POST   | Returns predicted class + confidence % |
| `/health`  | GET    | Returns `{"status": "ok"}`             |

---
