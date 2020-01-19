import json
import os
from typing import Dict, Union, List, Any
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

URI: Union[str, None] = os.getenv('MONGO_URI')
DATABASE_NAME: Union[str, None] = os.getenv('DATABASE_NAME')
COLLECTION_NAME: Union[str, None] = os.getenv('COLLECTION_NAME')
FARMERS_MARKET_RAW_DATA_PATH: Union[str, None] = os.getenv(
    'FARMERS_MARKET_RAW_DATA_PATH')


# connecting to Mongo Cluster Instance
client = MongoClient(URI)
db = client[DATABASE_NAME]
market_collection = db[COLLECTION_NAME]


with open(FARMERS_MARKET_RAW_DATA_PATH, mode='r') as infile:
    parsed_json: List[Any] = (json.loads(infile.read()))
    market_collection.insert_many(parsed_json)
