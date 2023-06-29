import csv
import sys
import pandas as pd


def filter_csv(file_name):
    count = 0
    with open(file_name,'r') as file :
        df = pd.read_csv(file)

        df['price'] = df['price'].replace('[\$\,\.]', '', regex=True).astype(int)
        df['Sales'] = df['price'] * df['quantity']

        output = df[df['product']== "pink morsel"]
        final_csv = df[['Sales','date','region']]
        print(final_csv)
        final_csv.to_csv('filterData.csv', mode='a', index=False, header=False)
        print("Data appended successfully.")
if __name__ == '__main__':
    filter_csv('./data/daily_sales_data_0.csv')
    filter_csv('./data/daily_sales_data_1.csv')
    filter_csv('./data/daily_sales_data_2.csv')
