# Airflow Lab_1

This lab demonstrates how Apache Airflow can orchestrate an end to end machine learning pipeline.

The pipeline loads e-commerce customer data, preprocesses it, trains a K-Means clustering model, finds the optimal number of clusters using elbow method.

## Dataset

- **ecommerce_customers.csv** — training data with 8,950 user transaction records
- **test_ecommerce.csv** — small test file with 2 rows
- **Features used:** `TOTAL_SPEND`, `BROWSE_SESSIONS`, `LOYALTY_POINTS`

**Prerequisites**

- Docker Desktop installed and running (at least 4 GB RAM allocated)
- Port 8080

## Steps to Re-Run the Lab

### Step 1: Create project folder

```bash
mkdir -p ~/app && cd ~/app
mkdir -p ./dags/src ./data ./config ./logs ./plugins ./working_data
```

### Step 2: Place files in the correct locations

- `airflow.py` → `dags/`
- `lab.py` and empty `__init__.py` → `dags/src/`
- `ecommerce_customers.csv` and `test_ecommerce.csv` → `data/`
- `airflow.cfg` → `config/`

### Step 3: Download Docker Compose file

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'
```

### Step 4: Edit docker-compose.yaml

Add these environment variables:

```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: "false"
AIRFLOW__CORE__ENABLE_XCOM_PICKLING: "true"
_PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:- pandas scikit-learn kneed matplotlib}
```

Add these volume mounts:

```yaml
- ${AIRFLOW_PROJ_DIR:-.}/data:/opt/airflow/dags/data
- ${AIRFLOW_PROJ_DIR:-.}/working_data:/opt/airflow/working_data
- ${AIRFLOW_PROJ_DIR:-.}/config/airflow.cfg:/opt/airflow/airflow.cfg
```

Set login credentials:

```yaml
_AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow2}
_AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow2}
```

### Step 5: Create .env file

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

### Step 6: Initialize and start Airflow

```bash
docker compose up airflow-init
docker compose up
```

Wait for the health check message, then open **http://localhost:8080** and log in with `airflow2` / `airflow2`.

### Step 7: Trigger the DAG

- Find **Ecommerce_Customer_Segmentation** in the DAGs list
- Toggle it on or click **Trigger DAG**
- Wait for all 5 tasks to turn green

### Step 8: Check outputs

- `model/model.sav` — trained K-Means model
- `working_data/elbow_curve.png` — elbow curve chart
- `working_data/cluster_scatter.png` — cluster scatter plot

### Step 9: Stop Airflow

```bash
docker compose down
```
