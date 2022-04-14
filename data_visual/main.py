import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
from os import environ
from time import process_time_ns
import psycopg2
from dotenv import load_dotenv
import seaborn as sb

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

        with connection.cursor() as cursor:

            '''Scatter chart'''
            # cursor.execute('select region.region, sum(total), year from employment inner join region on employment.region_id=region.id group by region.region, year order by sum(total)')

            # data = pd.DataFrame(cursor.fetchall())
            # print(data)


            # plt.scatter(data[0], data[1], c=data[2])
            # plt.title('Total amount of employers')
            # plt.xlabel('Region')
            # plt.ylabel('Amount in thousands')
            # plt.colorbar()
            # plt.show()



            '''Line chart'''
            # cursor.execute('select region.region, sum(total), year from employment inner join region on employment.region_id=region.id group by region.region, year order by region.region, year')

            # data = pd.DataFrame(cursor.fetchall())
            
            # region = data[0][0]
            # rows, l, legend = list(), list(), list()
            # for row in range(len(data[0])):

            #     if region != data[0][row]:
            #         legend.append(region)
            #         region = data[0][row]
            #         rows.append(l)
            #         l = list()
            #     else:
            #         l.append(data[1][row])
            # rows.append(l), legend.append(region)
                
            # print(len(rows))
            # for region in range(len(rows)):
            #     plt.plot(rows[region], label='list')
            # plt.title('Chart of employments in every regions')
            # plt.ylabel('Amount of employment in thousands')
            # plt.xlabel('Year')
            # plt.legend(legend)
            # plt.show()

            '''Bar Chart'''

            # cursor.execute('select region.region, sum(total) from employment inner join region on employment.region_id=region.id group by region.region order by region.region')

            # data = pd.DataFrame(cursor.fetchall())
            # plt.bar(data[0], data[1])
            # plt.show()


            # cursor.execute("select region.region, sum(total), year from employment inner join region on employment.region_id=region.id group by year, region.region having region.region='Emerging Europe Region' order by year")

            # data = pd.DataFrame(cursor.fetchall())
            # plt.plot(data[2], data[1])
            # # plt.title('Total Employment in Europe during 2000-2022')
            # # plt.legend('Europe')
            # plt.show()



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