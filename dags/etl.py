from datetime import datetime,timedelta
from airflow import DAG
import time
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd



# Define the DAG
default_args = {
    'owner': 'venkatesh',
}

def read_csv(**kwargs):
    ti = kwargs['ti']
    global sales_data, customers_data, products_data
    sales_data = pd.read_csv("/Users/apple/airflow/dags/datasets/sales.csv")
    customers_data = pd.read_csv("/Users/apple/airflow/dags/datasets/customers.csv")
    products_data = pd.read_csv("/Users/apple/airflow/dags/datasets/products.csv")
    print(sales_data.head())
    print(customers_data.head())
    print(products_data.head())
    ti.xcom_push(key='sales_data', value=sales_data.to_json())
    ti.xcom_push(key='customers_data', value=customers_data.to_json())
    ti.xcom_push(key='products_data', value=products_data.to_json())

def clean_data(**kwargs):
    ti = kwargs['ti']
    sales_data_json = ti.xcom_pull(task_ids='read_the_csv_files', key='sales_data')
    customers_data_json = ti.xcom_pull(task_ids='read_the_csv_files', key='customers_data')
    products_data_json = ti.xcom_pull(task_ids='read_the_csv_files', key='products_data')
    global sales_data, customers_data, products_data, clean_customers_data, clean_products_data, clean_sales_data
    sales_data = pd.read_json(sales_data_json)
    customers_data = pd.read_json(customers_data_json)
    products_data = pd.read_json(products_data_json)
    clean_sales_data = sales_data[(sales_data['sale_id'].notnull()) & (sales_data['product_id'].notnull())]
    clean_sales_data['sale_date'] = pd.to_datetime(clean_sales_data['sale_date'])
    clean_sales_data['sale_amount'] = pd.to_numeric(clean_sales_data['sale_amount'], errors='coerce')
    print(clean_sales_data.head())
    clean_customers_data = customers_data.drop_duplicates(subset=['customer_id']).dropna(subset=['customer_id'])
    print(clean_customers_data.head())
    clean_products_data = products_data.drop_duplicates(subset=['product_id']).dropna(subset=['product_id'])
    print(clean_products_data.head())
    ti.xcom_push(key='clean_sales_data', value=clean_sales_data.to_json())
    ti.xcom_push(key='clean_customers_data', value=clean_customers_data.to_json())
    ti.xcom_push(key='clean_products_data', value=clean_products_data.to_json())

def enrich_sales_data(**kwargs):
    ti = kwargs['ti']
    clean_sales_data_json = ti.xcom_pull(task_ids='clean_the_data', key='clean_sales_data')
    clean_customers_data_json = ti.xcom_pull(task_ids='clean_the_data', key='clean_customers_data')
    clean_products_data_json = ti.xcom_pull(task_ids='clean_the_data', key='clean_products_data')
    global clean_customers_data, clean_products_data, clean_sales_data, enriched_data, daily_sales
    clean_sales_data = pd.read_json(clean_sales_data_json)
    clean_customers_data = pd.read_json(clean_customers_data_json)
    clean_products_data = pd.read_json(clean_products_data_json)
    enriched_data = clean_sales_data.merge(clean_customers_data, on='customer_id', how='left')
    enriched_data = enriched_data.merge(clean_products_data, on='product_id', how='left')
    print(enriched_data.head())
    daily_sales = (enriched_data.groupby(['sale_date', 'category'])
                                .agg(total_sales=('sale_amount', 'sum'),
                                     total_transactions=('sale_id', 'count'))
                                .reset_index())
    print(daily_sales.head())
    ti.xcom_push(key='daily_sales_data', value=daily_sales.to_json())
    ti.xcom_push(key='enriched_data', value=enriched_data.to_json())

def compute_kpis(**kwargs):
    ti = kwargs['ti']
    daily_sales_json = ti.xcom_pull(task_ids='enrich_the_data', key='daily_sales_data')
    global daily_sales,kpis
    daily_sales=pd.read_json(daily_sales_json)
    kpis = (daily_sales.groupby('category')
                    .agg(total_revenue=('total_sales', 'sum'),
                         total_units_sold=('total_transactions', 'sum'))
                    .reset_index())
    print(kpis.head())
    ti.xcom_push(key='kpis_data', value=kpis.to_json())

def segment_customers(**kwargs):
    ti = kwargs['ti']
    clean_sales_data_json = ti.xcom_pull(task_ids='clean_the_data', key='clean_sales_data')
    clean_customers_data_json = ti.xcom_pull(task_ids='clean_the_data', key='clean_customers_data')
    global clean_sales, clean_customers
    clean_sales = pd.read_json(clean_sales_data_json)
    clean_customers = pd.read_json(clean_customers_data_json)
    customer_segmentation = (clean_sales.merge(clean_customers, on='customer_id', how='inner')
                                           .groupby(['customer_id', 'customer_name'])
                                           .agg(total_purchases=('sale_id', 'count'),
                                                total_spent=('sale_amount', 'sum'))
                                           .reset_index())
    customer_segmentation['segment'] = customer_segmentation['total_spent'].apply(
        lambda x: 'Premium' if x > 4000 else 'Regular' if x >= 2000 else 'Occasional')
    print(customer_segmentation.head())

with DAG(
    dag_id='executing_python_etl_dag',
    default_args=default_args,
    description='Using python etl code',
    schedule_interval='@daily',
    tags=['dependencies','python'],
    start_date= days_ago(1)
) as dag:
    read = PythonOperator(
        task_id='read_the_csv_files',
        python_callable=read_csv   
    )
    clean = PythonOperator(
        task_id='clean_the_data',
        python_callable=clean_data 
    )
    enrich = PythonOperator(
        task_id='enrich_the_data',
        python_callable=enrich_sales_data   
    )
    compute = PythonOperator(
        task_id='compute_KPIs_for_the_data',
        python_callable=compute_kpis   
    )
    segmentation = PythonOperator(
        task_id='Segementation',
        python_callable=segment_customers   
    )

read>>clean>>enrich>>compute>>segmentation
