
#submit jobs
gcloud dataproc jobs submit pyspark Spark-Job/spark_job1.py \
--cluster=${week3-dataproc} \
--region="asia-southeast2-a" \
-- gs://${week3-spark-etl}/all_flight_data/all_flight_data.csv