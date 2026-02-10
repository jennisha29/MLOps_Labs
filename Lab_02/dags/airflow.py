from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from src.lab import (
    load_data,
    data_preprocessing,
    build_save_model,
    load_model_elbow,
    generate_visualizations,
)
 
default_args = {
    "owner": "Jennisha Martin",
    "start_date": datetime(2026, 2, 1),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="Ecommerce_Customer_Segmentation",
    default_args=default_args,
    description="E-commerce customer segmentation using KMeans + elbow method",
    schedule_interval=None,
    catchup=False,
) as dag:

    # loading the e-commerce dataset
    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data,
    )
    
    data_preprocessing_task = PythonOperator(
        task_id="data_preprocessing_task",
        python_callable=data_preprocessing,
        op_args=[load_data_task.output],
    )

    # training KMeans model
    build_save_model_task = PythonOperator(
        task_id="build_save_model_task",
        python_callable=build_save_model,
        op_args=[data_preprocessing_task.output, "model.sav"],
    )
    # applying elbow method
    load_model_task = PythonOperator(
        task_id="load_model_task",
        python_callable=load_model_elbow,
        op_args=["model.sav", build_save_model_task.output],
    )
    # creating visualization plots
    visualize_task = PythonOperator(
        task_id="generate_visualizations_task",
        python_callable=generate_visualizations,
        op_args=[load_model_task.output],
    )

    load_data_task >> data_preprocessing_task >> build_save_model_task >> load_model_task >> visualize_task

if __name__ == "__main__":
    dag.test()