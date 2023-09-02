FROM apache/airflow:2.7.0
ADD requirements.txt . 
ADD extract.py .
ADD transform.py .
ADD load.py .
ADD defaults.py .
ADD .env .
RUN pip install apache-airflow==2.7.0 -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/"