# Apache Airflow Project

## Overview

This project demonstrates executing **multiple dependent DAGs** in Apache Airflow. Airflow is an open-source platform to programmatically author, schedule, and monitor workflows.

The project highlights:
- Task dependencies and parallel execution.
- Task execution monitoring with logs and UI visualization.
- Use of **BashOperator** for task execution.

---

## DAG Details

- **DAG Name**: `executing_multiple_dags`
- **Tasks**:
    - `task_a`
    - `task_b`
    - `task_c`
    - `task_d`

### Task Dependency

- `task_a` triggers both `task_b` and `task_c` in parallel.
- After the successful execution of `task_b` and `task_c`, `task_d` executes.

---

## DAG Visualization

### Task Flow

The graph view below shows the dependency structure:

![Graph View](images/Screenshot-2024-12-15-at-1.44.07PM.png)

---

## Task Monitoring

### Task Execution States

- **Green**: Success
- **Red**: Failed
- **Yellow**: Running or Retry

The task duration chart below shows task states and durations:

![Task Execution Overview](images/Screenshot-2024-12-15-at-1.44.25PM.png)

---

## Execution Logs

Detailed logs can be accessed in the Airflow UI to track task outputs and debug errors. Here is an example log from `task_a`:

![Logs](images/Screenshot-2024-12-14-at-8.41.37PM.png)

**Sample Log Output**:
```bash
INFO - task_A has started
INFO - Task A printing 1
INFO - Task A printing 2
INFO - Task A printing 3
...
INFO - Task A printing 10
INFO - task_A has ended!!



Here is the GitHub-compatible README.md code for your Apache Airflow project. It includes Markdown syntax and assumes the images are stored in an images folder within your repository.

markdown
Copy code
# Apache Airflow Project

## Overview

This project demonstrates executing **multiple dependent DAGs** in Apache Airflow. Airflow is an open-source platform to programmatically author, schedule, and monitor workflows.

The project highlights:
- Task dependencies and parallel execution.
- Task execution monitoring with logs and UI visualization.
- Use of **BashOperator** for task execution.

---

## DAG Details

- **DAG Name**: `executing_multiple_dags`
- **Tasks**:
    - `task_a`
    - `task_b`
    - `task_c`
    - `task_d`

### Task Dependency

- `task_a` triggers both `task_b` and `task_c` in parallel.
- After the successful execution of `task_b` and `task_c`, `task_d` executes.

---

## DAG Visualization

### Task Flow

The graph view below shows the dependency structure:

![Graph View](images/Screenshot-2024-12-15-at-1.44.07PM.png)

---

## Task Monitoring

### Task Execution States

- **Green**: Success
- **Red**: Failed
- **Yellow**: Running or Retry

The task duration chart below shows task states and durations:

![Task Execution Overview](images/Screenshot-2024-12-15-at-1.44.25PM.png)

---

## Execution Logs

Detailed logs can be accessed in the Airflow UI to track task outputs and debug errors. Here is an example log from `task_a`:

![Logs](images/Screenshot-2024-12-14-at-8.41.37PM.png)

**Sample Log Output**:
```bash
INFO - task_A has started
INFO - Task A printing 1
INFO - Task A printing 2
INFO - Task A printing 3
...
INFO - Task A printing 10
INFO - task_A has ended!!
Prerequisites
Ensure the following are installed:

Python 3.8+
Apache Airflow 2.x
Airflow environment is properly configured.
Steps to Run the Project
Clone the Repository:

bash
Copy code
git clone https://github.com/VenkateshAddala/Apache-Airflow-project.git
cd Apache-Airflow-project
Install Apache Airflow:

bash
Copy code
pip install apache-airflow
Initialize Airflow:

Initialize the database:
bash
Copy code
airflow db init
Create an admin user:
bash
Copy code
airflow users create \
  --username admin \
  --firstname CloudUser \
  --lastname Addala \
  --role Admin \
  --email venkatesh.addala@gmail.com
Start Airflow Services:

Start the scheduler:
bash
Copy code
airflow scheduler &
Start the webserver:
bash
Copy code
airflow webserver
Run the DAG:

Copy the executing_multiple_dags.py to your Airflow DAGs directory.
Access the Airflow UI at http://localhost:8080.
Enable and trigger the DAG executing_multiple_dags.
