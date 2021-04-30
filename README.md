# ETL on Google Cloud Platform Using PySpark & Dataproc

## Case:

<p align="center">
<img width="671" alt="Screen Shot 2021-04-30 at 22 42 47" src="https://user-images.githubusercontent.com/22974798/116719601-72a66d00-aa05-11eb-9e6b-3c2ff2cec135.png">
</p>

## Stack

### PySpark
PySpark is an interface for Apache Spark in Python which allows you to write Spark application in Python API. Common methods of pandas for data transformation are doable in PySpark. PySpark is commonly used to handle big data.

### Dataproc
How do we run PySpark script in Google Cloud? By using Dataproc. Dataproc is a fully managed and highly scalable service for running Apache Spark, Apache Flink, Presto, and 30+ open source tools and frameworks. For complete gude, check this [link](https://cloud.google.com/dataproc)

### Dataset
The dataset are provided on JSON file format.
<p align="center">
  <img width="1206" alt="Screen Shot 2021-04-30 at 22 48 26" src="https://user-images.githubusercontent.com/22974798/116720495-75559200-aa06-11eb-9341-5b2ee63abbdf.png">
</p>

## Installation
Clone this repository on your Google Cloud Shell

```
git init
git clone https://github.com/abdikaalbiyan/Spark-Job
cd Spark-Job
```

## How to Use

1. Create a Bucket on Google Cloud Storage
<p align="center">
  <img width="543" alt="Screen Shot 2021-04-30 at 22 55 08" src="https://user-images.githubusercontent.com/22974798/116721118-29efb380-aa07-11eb-99fa-f1e9a214b678.png">
</p><br>
2. Upload a folder contains some of Json data format.
<p align="center">
  <img width="730" alt="Screen Shot 2021-04-30 at 22 58 06" src="https://user-images.githubusercontent.com/22974798/116721508-95398580-aa07-11eb-8014-bc3c3d1d67bf.png">
</p><br>
3. Run ```python union_files.py```<br>
&nbsp &nbsp This process will union all the dataset and store them to ***/all_flight_data/*** directory as a csv file.<br>
4. Copy & paste spark_job1.py to gs bucket
