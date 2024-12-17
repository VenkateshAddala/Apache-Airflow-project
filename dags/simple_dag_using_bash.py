from datetime import datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator



# Define the DAG
default_args = {
    'owner': 'venkatesh',
}

with DAG(
    dag_id='executing_multiple_dags',
    default_args=default_args,
    description='executing multiple jobs having dependency',
    schedule_interval='@once',
    start_date= days_ago(1)
) as dag:

    taskA = BashOperator(
        task_id='task_a',
        bash_command='''
        echo task_A has started
        for i in {1..10}
        do
            echo Task A printing $i
        done

        echo task_A has ended!!
        '''
    )
    taskB = BashOperator(
        task_id='task_b',
        bash_command='''
        echo task_B has started
        sleep 15
        echo task_B has ended!!
        '''
    )
    taskC = BashOperator(
        task_id='task_c',
        bash_command='''
        echo task_C has started
        sleep 5
        echo task_C has ended!!
        '''
    )
    taskD = BashOperator(
        task_id='task_d',
        bash_command='''
        echo task_D has completed!!
        '''
    )

taskA>>taskB
taskA>>taskC

taskB>>taskD
taskC>>taskD


# taskA.set_downstream(taskB)
# Define task dependencies (optional for a single task)
# hello_task
# hello_task = PythonOperator(
    #     task_id='hello_world_task',
    #     python_callable=hello_world,
    #     dag=dag
    # )

