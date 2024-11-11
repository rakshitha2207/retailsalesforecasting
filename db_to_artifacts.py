import os
import pandas as pd
from pymongo import MongoClient

class SalesData:
    def __init__(self):
        # Load environment variables
        self.MONGO_URI = os.environ['MONGO_URI']

        # Create a MongoDB client using the URI
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client.get_default_database()  # This gets the default database based on the URI

    # function to query data from the database and return a DataFrame
    def save_sales_data(self, filepath):
        sales_collection = self.db['retail_sales']  # Assuming 'retail_sales' is your collection name
        query = {"sales_date": {"$gte": pd.Timestamp('2023-05-01')}}
        results = sales_collection.find(query)

        # Convert results to a DataFrame
        sales_df = pd.DataFrame(list(results))

        # check if there are new observations in the sales_df
        if not sales_df.empty:
            if '_id' in sales_df.columns:
                sales_df = sales_df.drop('_id', axis=1)
            sales_df['sales_date'] = pd.to_datetime(sales_df['sales_date'])
            sales_df.set_index('sales_date', inplace=True)
            sales_df.index = pd.date_range(start=sales_df.index.min(), end=sales_df.index.max(), freq='MS')

            # Read test.csv file
            test = pd.read_csv(filepath, index_col=0, parse_dates=True)
            # Append new data points to the test set
            test = pd.concat([test, sales_df])

            # Save the test.csv file to the specified filepath
            test.to_csv(filepath, index=True)
            print('New sales data has been added to the test set')
        else:
            print('No new sales data has been added to the test set')

    # function to close the database connection
    def close(self):
        self.client.close()

# Specify the path where the test.csv file should be saved
filepath = 'artifacts/test.csv'

# Create an instance of the SalesData class
sales_data = SalesData()

# Retrieve the new sales data records and save it as a CSV file
sales_data.save_sales_data(filepath)

# Close the database connection
sales_data.close()
