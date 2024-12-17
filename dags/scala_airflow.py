from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# Default arguments for the DAG
default_args = {
    'owner': 'venkatesh'
}

# Define the DAG
with DAG(
    dag_id='execute_spark_jar_with_main_class',
    default_args=default_args,
    description='Run a Scala Spark JAR file with a specific main Java class using Airflow',
    schedule_interval=None,  # Set as per your schedule
    start_date=datetime(2024, 12, 14)
) as dag:
    
    run_jar_task = SparkSubmitOperator(
    task_id='run_scala_jar_with_class',
    application='/Users/apple/airflow/dags/jar/scalaspark_2.13-0.1.0-SNAPSHOT.jar',  # Path to the JAR file
    name='scala_jar_execution_with_class',
    conn_id='spark_default',  # Spark connection in Airflow
    application_args=['arg1', 'arg2'],  # Replace with actual arguments if required
    java_class='org.scala.example.IngestJob',  # Replace with your actual Java class name
    dag=dag,
    driver_memory="1g",
    executor_cores=1,
    num_executors=1,
    executor_memory='1g'
)

# Set up dependencies
run_jar_task
