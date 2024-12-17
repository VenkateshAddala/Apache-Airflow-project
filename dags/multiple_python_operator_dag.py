from datetime import datetime,timedelta
from airflow import DAG
import time
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator



# Define the DAG
default_args = {
    'owner': 'venkatesh',
}

def sample_funA(name,city):
    print("Inside sample A python function!")
    print("hello, {name} from {city}".format(name=name,city=city))

def sample_funB():
    time.sleep(10)
    print("Inside sample B python function!")

def sample_funC():
    print("Inside sample C python function!")

def sample_funD():
    print("Inside sample D python function!")


with DAG(
    dag_id='executing_python_operators_dag',
    default_args=default_args,
    description='Using python operator in dag',
    schedule_interval='@daily',
    tags=['dependencies','python'],
    start_date= days_ago(1)
) as dag:
    taskA = PythonOperator(
        task_id='SampleA_function',
        python_callable=sample_funA,
        op_kwargs={'name':'Venkatesh','city':'San Fransisco'}
    ) 
    taskB = PythonOperator(
        task_id='SampleB_function',
        python_callable=sample_funB
    )
    taskC = PythonOperator(
        task_id='SampleC_function',
        python_callable=sample_funC
    )
    taskD = PythonOperator(
        task_id='SampleD_function',
        python_callable=sample_funD
    )

taskA>>[taskB,taskC]
[taskB,taskC] >>taskD
