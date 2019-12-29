import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator

import datetime

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retires': 1,
    'retry_delay': datetime.timedelta(seconds=5),
    'start_date': airflow.utils.dates.days_ago(0),
    'sla' : datetime.timedelta(minutes=20)
}

dag = DAG(
    dag_id='printSomething',
    default_args=args,
    schedule_interval=None,
    catchup=False,
)

def printSomething(**context):
    date = context['execution_date']
    conf = context['dag_run'].conf['key']
    print(conf)
    print(date)
    return date

t1 = PythonOperator(
    task_id='printSomething',
    python_callable=printSomething,
    provide_context=True,
    dag=dag
)

t4 = DummyOperator(
    task_id='complete',
    trigger_rule='one_success',
    dag=dag
)

t1 >> t4