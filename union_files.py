import pandas as pd
import numpy as np


def main():

    data1 = pd.read_json('gs://week3-spark-etl/json-files/2021-04-27.json', lines=True)
    data1.drop('id', inplace=True, axis=1)
    data1.loc[data1['flight_date'] == '2019-05-04', 'flight_date'] = '2021-04-26'

    data2 = pd.read_json('gs://week3-spark-etl/json-files/2021-04-28.json', lines=True)
    data2.drop('id', inplace=True, axis=1)
    data2.loc[data2['flight_date'] == '2019-05-05', 'flight_date'] = '2021-04-27'

    data3 = pd.read_json('gs://week3-spark-etl/json-files/2021-04-29.json', lines=True)
    data3.drop('id', inplace=True, axis=1)
    data3.loc[data3['flight_date'] == '2019-05-06', 'flight_date'] = '2021-04-28'

    data4 = pd.read_json('gs://week3-spark-etl/json-files/2021-04-30.json', lines=True)
    data4.drop('id', inplace=True, axis=1)
    data4.loc[data4['flight_date'] == '2019-05-07', 'flight_date'] = '2021-04-29'

    all_flight_data = pd.concat([data1, data2, data3, data4])

    all_flight_data.to_csv('gs://week3-spark-etl/all_flight_data/all_flight_data.csv', index = False, header=True)


if __name__=="__main__":
	main()