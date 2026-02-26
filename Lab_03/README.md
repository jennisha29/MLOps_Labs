# Lab_03 — Docker

A machine learning pipeline that trains a **Gradient Boosting Regressor** on the
California Housing dataset to predict median house prices, built and run entirely
inside a Docker container.

---

## Overview

Loading the California Housing dataset (20,640 districts), training a regression model,
evaluating it, and saving three output artifacts to the local machine:

- `california_gbr_model.pkl` — the trained model
- `metrics.json` — MSE and R² scores
- `feature_importance.json` — which features drive house prices most

---

## Project Structure

```
Lab_03/
├── src/
│   └── main.py               # trains model, saves all 3 outputs
├── test/
│   └── test_model.py         # 12 unit tests
├── data/                     # outputs appear here after docker run
│   ├── california_gbr_model.pkl
│   ├── metrics.json
│   └── feature_importance.json
├── dashboard/
│   └── dashboard.html        # visual results dashboard
├── Dockerfile
├── requirements.txt
├── README.md
└── SETUP.md                  # step-by-step run instructions
```

---

## Results

| Metric        | Value                                                   |
| ------------- | ------------------------------------------------------- |
| R²            | 0.7756 — model explains ~77.6% of price variation       |
| MSE           | 0.2940                                                  |
| Tests         | 12 / 12 passed                                          |
| Image size    | ~126MB                                                  |
| Top predictor | `MedInc` — median income drives prices the most (60.4%) |

---

## Dashboard

After running the container, open the dashboard to see the results:

```bash
python3 -m http.server 8000
```

Then open: `http://localhost:8000/dashboard/dashboard.html`
