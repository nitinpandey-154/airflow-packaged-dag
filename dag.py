from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from my_package import list_files

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 4, 17),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(dag_id='test_dag', default_args=default_args, schedule_interval='0 0 * * *') as dag:
    bo = BashOperator(
        task_id='print_date',
        bash_command='date')

    po = PythonOperator(task_id="list_files", python_callable=list_files)

    bo >> po
