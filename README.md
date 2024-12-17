Apache Airflow Project
Overview
This project demonstrates how to execute multiple dependent DAGs (Directed Acyclic Graphs) in Apache Airflow. Airflow is an open-source platform to programmatically author, schedule, and monitor workflows.

The project is designed to:

Showcase task dependencies.
Demonstrate execution logs and monitoring features.
Use BashOperator to execute basic tasks.
Project Details
DAG Name: executing_multiple_dags

Tasks:

task_a
task_b
task_c
task_d
Task Dependency:

task_a triggers both task_b and task_c.
Once task_b and task_c succeed, task_d will execute.
DAG Visualization
The graph view shows how the tasks are connected.


Here, the DAG executes with the following flow:

task_a starts.
After task_a completes, both task_b and task_c execute in parallel.
Once task_b and task_c succeed, task_d executes.
Task Monitoring
You can monitor task states and logs using Airflow’s user interface.

Task Execution States:
Green: Success
Red: Failed
Yellow: Running or Retries
Below is the task execution overview.


Logs Example
You can view detailed logs for each task to debug and monitor execution. Logs for task_a are shown below.


Sample Log Output:

bash
Copy code
INFO - task_A has started
INFO - Task A printing 1
INFO - Task A printing 2
INFO - Task A printing 3
INFO - Task A printing 4
...
INFO - Task A printing 10
INFO - task_A has ended!!
Prerequisites
Python 3.8+
Apache Airflow 2.x
A running Airflow environment.
Steps to Run the Project
Clone the Repository:

bash
Copy code
git clone https://github.com/VenkateshAddala/Apache-Airflow-project.git
cd Apache-Airflow-project
Set Up Airflow:

Install Airflow:
bash
Copy code
pip install apache-airflow
Initialize the Airflow database:
bash
Copy code
airflow db init
Create a user:
bash
Copy code
airflow users create \
  --username admin \
  --firstname CloudUser \
  --lastname Addala \
  --role Admin \
  --email venkatesh.addala@gmail.com
Start Airflow Scheduler and Webserver:

bash
Copy code
airflow scheduler &
airflow webserver
Add the DAG:

Place the executing_multiple_dags.py file in your Airflow DAGs directory.
Run the DAG:

Open the Airflow UI at http://localhost:8080.
Trigger the DAG named executing_multiple_dags.
Key Highlights
Task Dependency Visualization: Clear task flow using Airflow’s graph view.
Task Execution Logs: Detailed logs to track task execution.
Real-World Workflow Representation: A sample DAG for multiple interdependent tasks.
Screenshots
Below are the screenshots illustrating different views:

Task Graph View

Task Execution Logs

Task Duration and Overview

Conclusion
This project is a demonstration of executing multiple tasks in Apache Airflow with dependencies, logs, and visual monitoring. It helps users understand how to design workflows, monitor task states, and debug executions effectively.

Author
Venkatesh Addala
