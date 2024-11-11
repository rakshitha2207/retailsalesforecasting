import pandas as pd
import os
from fredapi import Fred
from pymongo import MongoClient
from datetime import datetime

class FredToMongoDB:
    def __init__(self, fred_api_key, mongo_uri, db_name, collection_name):
        # Initialize FRED API and MongoDB connection parameters
        self.fred_api_key = fred_api_key
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.collection_name = collection_name

    def get_sales(self):
        # Fetch retail sales data from FRED API
        fred = Fred(api_key=self.fred_api_key)
        retail_sales = fred.get_series('RSXFSN', observation_start='2023-05-01') / 1000  # Convert from millions to billions

        # Convert to DataFrame and format
        df = pd.DataFrame(retail_sales, columns=['sales_amount'])
        df.index = pd.to_datetime(df.index)
        df.index.freq = 'MS'  # Monthly frequency

        # Transform data into a list of dictionaries for MongoDB
        sales_data = [
            {
                "sales_date": datetime(year=index.year, month=index.month, day=1),
                "sales_amount": float(sales)
            }
            for index, sales in df.itertuples()
        ]
        return sales_data

    def store_sales(self, sales_data):
        # Connect to MongoDB
        client = MongoClient(self.mongo_uri)
        db = client[self.db_name]
        collection = db[self.collection_name]

        # Insert data if it doesn't already exist (by sales_date)
        for record in sales_data:
            collection.update_one(
                {"sales_date": record["sales_date"]},  # Find record by sales_date
                {"$setOnInsert": record},  # Insert only if not present
                upsert=True
            )

        # Close the connection
        client.close()

# Initialize FredToMongoDB with necessary credentials
fred_to_mongo = FredToMongoDB(
    fred_api_key=os.getenv("FRED_API_KEY"),                 # FRED API Key
    mongo_uri=os.getenv("MONGO_URI"),                       # MongoDB URI
    db_name="sales_data_db",                                # Database name
    collection_name="retail_sales"                          # Collection name
)

# Fetch sales data from FRED and store in MongoDB
sales_data = fred_to_mongo.get_sales()
fred_to_mongo.store_sales(sales_data)
