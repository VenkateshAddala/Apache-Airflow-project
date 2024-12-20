# Apache Airflow Project: Python ETL DAG

## Overview

This project demonstrates an **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow** with Python code. It is designed to process CSV files, clean and enrich data, compute KPIs, and perform data segmentation. The project showcases the power of Airflow's PythonOperator and XComs to enable seamless data processing workflows.

---

## DAG Details

- **DAG Name**: `executing_python_etl_dag`
- **Tasks**:
    - `read_the_csv_files`: Reads input CSV files.
    - `clean_the_data`: Cleans the customer, product, and sales data.
    - `enrich_the_data`: Enriches data by merging datasets.
    - `compute_KPIs_for_the_data`: Computes Key Performance Indicators (KPIs).
    - `Segmentation`: Segments data based on customer activity.

---

## DAG Visualization

### Task Dependency Flow

The DAG flow ensures dependencies are maintained between tasks. Below is the graph view of the DAG:

<img width="1466" alt="Screenshot 2024-12-19 at 6 38 05 PM" src="https://github.com/user-attachments/assets/14519d0d-f9ed-418e-b02e-1de4467a022d" />


### Task Execution States

The task execution overview shows:
- Green: Success
- Red: Failed
- Yellow: Running or Retry


---

## Data Processing Steps

1. **Extract Data**:
    - Reads customer, product, and sales data from CSV files using the `read_the_csv_files` task.
    - Outputs raw data for further processing.

    **XCom Output Example**:
    <img width="1461" alt="Screenshot 2024-12-19 at 6 39 30 PM" src="https://github.com/user-attachments/assets/553042d3-062e-4196-9d08-76f76c3223f4" />

2. **Transform Data**:
    - Cleans raw data (e.g., removes null values) via the `clean_the_data` task.
    - Enriches data by merging datasets using the `enrich_the_data` task.

    **Enriched Data Example**:
    <img width="1464" alt="Screenshot 2024-12-19 at 7 03 36 PM" src="https://github.com/user-attachments/assets/09e9cbdd-09a8-4ff8-b7af-69c12b1426cf" />


3. **Compute KPIs**:
    - Calculates KPIs such as `total_revenue` and `total_units_sold` using the `compute_KPIs_for_the_data` task.

    **KPIs Example**:
    <img width="1460" alt="Screenshot 2024-12-19 at 7 03 55 PM" src="https://github.com/user-attachments/assets/d29990c6-c361-4911-aa0d-3b5046e9711d" />


4. **Load Data**:
    - Segments customers based on KPIs via the `Segmentation` task.
    <img width="1462" alt="Screenshot 2024-12-19 at 7 04 17 PM" src="https://github.com/user-attachments/assets/f68f5038-95b4-47ed-8f5b-bdffb605c750" />

---

## Execution Logs

Logs are available for each task to debug and monitor execution. Below is an example from the `Segmentation` task:

<img width="1462" alt="Screenshot 2024-12-19 at 7 04 17 PM" src="https://github.com/user-attachments/assets/f68f5038-95b4-47ed-8f5b-bdffb605c750" />


**Sample Log Output**:
```plaintext
INFO - Starting segmentation task
INFO - Segmented customers into:
    Premium
    Occasional
INFO - Segmentation completed successfully
