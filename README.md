# ETL on Google Cloud Platform Using PySpark & Dataproc

## Flow:

<p align="center">
<img width="805" alt="Screen Shot 2021-05-06 at 15 52 58" src="https://user-images.githubusercontent.com/22974798/117270261-3a7ab080-ae83-11eb-992f-6a5ab378c365.png">

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
3. Run 
   ```
   python union_files.py
   ```
   <br>
&nbsp &nbsp This process will union all the dataset and store them to ***/all_flight_data/*** directory as a csv file.<br><br>
4. Copy & paste spark_job1.py to gs bucket<br>
5. Create e Dataproc Cluster
 <p align="center">
  <img width="944" alt="Screen Shot 2021-04-30 at 23 30 22" src="https://user-images.githubusercontent.com/22974798/116725504-2ad71400-aa0c-11eb-9fd9-d80ca6a1945c.png">
  </p>
7. Submit a Dataproc job inside Cluster with spark_job1.py as a Main Python File
 <p align="center">
  <img width="611" alt="Screen Shot 2021-04-30 at 23 22 23" src="https://user-images.githubusercontent.com/22974798/116724507-f1ea6f80-aa0a-11eb-9793-99ae9436586d.png">
  </p>
  
  
## Result

### Job detail
 <p align="center">
  <img width="1259" alt="Screen Shot 2021-04-30 at 23 24 26" src="https://user-images.githubusercontent.com/22974798/116725876-be104980-aa0c-11eb-8ffd-f70471976434.png">
</p>

### BigQuery
<p align="center">
  <img width="512" alt="Screen Shot 2021-04-30 at 23 38 27" src="https://user-images.githubusercontent.com/22974798/116726249-3840ce00-aa0d-11eb-9d9f-1e6563021a1d.png">

  </p>


