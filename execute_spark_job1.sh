
#submit jobs
gcloud dataproc jobs submit pyspark spark_job1.py \
--cluster=${week3-dataproc} \
--region="asia-southeast2-a" \
--jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar \
-- gs://${week3-spark-etl}/$(date '+%Y-%m-%d').json