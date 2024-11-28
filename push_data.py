import os 
import sys
import json
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, filepath):
        try:
            data = pd.read_csv(filepath)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILEPATH = "Network_Data\phisingData.csv"
    DATABASE = "KOSISO"
    Collection = "NetworkData"

    network= NetworkDataExtract()
    records = network.csv_to_json_converter(FILEPATH)
    no_of_records = network.insert_data_to_mongodb(records,DATABASE, Collection)
    print(no_of_records)