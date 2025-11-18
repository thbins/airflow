import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG (
    dag_id="dags_bash_with_macro_eg2",
    schedule="10 0 * * 6#2", # 매월 둘째 토요일 0시 10분
    start_date=pendulum.datetime(2025, 9, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    # START_DATE: 2주전 월요일, END_DATE: 2주전 토요일
    bask_task_1 = BashOperator(
        task_id="bash_task_1",
        env={'START_DATE':'{{ (date_interval_start.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=19)) | ds }}',
             'END_DATE':'{{ (date_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=14)) | ds }}'
             },
        bash_command='echo "START_DATE: $START_DATE && END_DATE: $END_DATE"'
    )