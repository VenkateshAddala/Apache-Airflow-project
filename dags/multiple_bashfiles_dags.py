from datetime import datetime,timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator



# Define the DAG
default_args = {
    'owner': 'venkatesh',
}

with DAG(
    dag_id='multiple_dags',
    default_args=default_args,
    description='executing multiple jobs',
    schedule_interval=timedelta(days=1),
    tags=['scripts','template search'],
    template_searchpath='/Users/apple/airflow/dags/bash_scripts',
    start_date= days_ago(1)
) as dag:

    taskA = BashOperator(
        task_id='task_a',
        bash_command='taskA.sh'
    )
    taskB = BashOperator(
        task_id='task_b',
        bash_command='taskB.sh'
    )
    taskC = BashOperator(
        task_id='task_c',
        bash_command='taskC.sh'
    )
    taskD = BashOperator(
        task_id='task_d',
        bash_command='taskD.sh'
    )
    taskE = BashOperator(
        task_id='task_e',
        bash_command='taskE.sh'
    )
    taskF = BashOperator(
        task_id='task_f',
        bash_command='taskF.sh'
    )
    taskG = BashOperator(
        task_id='task_g',
        bash_command='taskG.sh'
    )

taskA>>taskB>>taskE
taskA>>taskC>>taskF
taskA>>taskD>>taskG



