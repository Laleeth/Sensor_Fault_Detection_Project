import logging
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import os
import sys

if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print("connection name", mongodb_client.database.list_collection_names())






# def test_exception():
#     try:
#         logging.info("We are trying to divide")
#         x = 1/0
#     except Exception as e:
#         raise SensorException(e, sys)


# if __name__ == '__main__':
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)

    # mongodb_client = MongoDBClient()
    # print("connection name", mongodb_client.database.list_collection_names())
