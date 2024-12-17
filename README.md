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


<img width="1457" alt="Screenshot 2024-12-15 at 1 44 07 PM" src="https://github.com/user-attachments/assets/981518e6-c7bf-4be1-a866-cfca3d3478c7" />


---

## Task Monitoring

### Task Execution States

- **Green**: Success
- **Red**: Failed
- **Yellow**: Running or Retry

The task duration chart below shows task states and durations:


---

## Execution Logs

Detailed logs can be accessed in the Airflow UI to track task outputs and debug errors. Here is an example log from `task_a`:


<img width="1457" alt="Screenshot 2024-12-15 at 1 44 25 PM" src="https://github.com/user-attachments/assets/1fc67a33-3191-44fe-9616-07b572628299" />


**Sample Log Output**:
```bash
INFO - task_A has started
INFO - Task A printing 1
INFO - Task A printing 2
INFO - Task A printing 3
...
INFO - Task A printing 10
INFO - task_A has ended!!

INFO - Task A printing 3
...
INFO - Task A printing 10
INFO - task_A has ended!!

