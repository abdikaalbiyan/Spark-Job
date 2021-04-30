from datetime import date
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

from pyspark.conf import SparkConf
from pyspark.sql.session import SparkSession


sc      = SparkContext()
spark   = SQLContext(sc)


bucket_name  = "gs://week3-spark-etl"
flights_data = spark.read.format("csv").option("header",True).load(bucket_name+"/all_flight_data/all_flight_data.csv")

flights_data.registerTempTable("flights_data")


all_flight_data_query = """
        SELECT
            flight_date,
            airline_code,
            flight_num,
            source_airport,
            destination_airport,
            departure_time,
            departure_delay,
            arrival_time,
            arrival_delay,
            airtime,
            distance
        FROM
            flights_data
        ORDER BY
            flight_date ASC,
            flight_num ASC
        """

avg_delays_by_flight_nums_query = """
        SELECT
            flight_num,
            flight_date,
            round(avg(arrival_delay),2) as avg_arrival_delay,
            round(avg(departure_delay),2) as avg_departure_delay 
        FROM
            flights_data
        GROUP BY
            flight_date,
            flight_num
        ORDER BY
            flight_date ASC,
            (avg_arrival_delay + avg_departure_delay) DESC
        """

dataframe_all_flight_data           = spark.sql(all_flight_data_query)
dataframe_avg_delays_by_flight_nums = spark.sql(avg_delays_by_flight_nums_query)


#Load data to BigQuery table
dataframe_all_flight_data.write \
            .format("bigquery") \
            .option("table","light_dataset.master_flight_data") \
            .mode("append") \
            .save()

dataframe_avg_delays_by_flight_nums.write \
            .format("bigquery") \
            .option("table","light_dataset.avg_delays_by_flight_nums") \
            .mode("append") \
            .save()



output_flight = bucket_name+"/output_flight"

dataframe_avg_delays_by_flight_nums.coalesce(1).write.format("json").save(output_flight)

