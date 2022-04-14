import os
import csv
import pandas as pd
import matplotlib
from os import environ
from time import process_time_ns
import psycopg2
from dotenv import load_dotenv

load_dotenv()

initial_data = './initial_data.csv'
region_data = './region.csv'

data = pd.read_csv(region_data)



def make_queries():
    region_data = './region.csv'
    try:
        connection = psycopg2.connect(
            host=os.getenv('host'),
            port=os.getenv('port'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            dbname=os.getenv('db_name')
        )

        connection.autocommit = True

        '''Add new col region'''
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         'SELECT DISTINCT country FROM employment;'
        #     )
        #     region_data = pd.read_csv(region_data)
        #     data = pd.DataFrame(cursor.fetchall())

        #     for country in data[0]:
        #         country = country.replace("'", "''")
        #         for region in region_data:
        #             if region[0] != 'U':
        #                 if (country in region_data[region].values or country + ' ' in region_data[region].values) and region != 'ALL Countries':
        #                     cursor.execute(f"UPDATE employment SET region_id=reg_id.id\
        #                         FROM(SELECT id FROM region WHERE region='{region}') as reg_id WHERE country='{country}';")
        #                     print(country, region)
                        

 

        '''Create initial data'''
        # with open(initial_data, newline='') as data:
        #     csv_data = csv.reader(data, delimiter=',')
            
        #     country = str()
        #     with connection.cursor() as cursor:
        #         for row in csv_data:
        #             country = row[1].replace("'", "''").rstrip()
        #             cursor.execute(
        #                 f"INSERT INTO employment\
        #                 VALUES ({id}, '{country}', {row[2]}, {row[3]}, {row[4]},\
        #                     {row[5]}, {row[6]}, {row[7]}, {row[8]},\
        #                         {row[9]}, {row[10]}, {row[11]});"
        #             )
        #             connection.commit()

    except Exception as _ex:
        print(_ex)

    finally:
        connection.close


make_queries()