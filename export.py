#!/usr/bin/python
# Author: Jan van Unnik

import logging
import os
from google.cloud import storage
from config import root

#set enviroment variable to load location of authentication file for Google Cloud API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/pi/temperature/apikey.json'

bucket_name = "zwaanshals"
source_file_name_1 = root+"output/temperature.csv"
destination_blob_name_1 = "temperatuur.csv"
source_file_name_2 = root+"output/latest.csv"
destination_blob_name_2 = "latest.csv"

def upload_blob(bucket_name, source_file_name_1, source_file_name_2, destination_blob_name_1, destination_blob_name_2):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob1 = bucket.blob(destination_blob_name_1)
    blob2 = bucket.blob(destination_blob_name_2)

    blob1.upload_from_filename(source_file_name_1)
    blob2.upload_from_filename(source_file_name_2)

    print('File {} uploaded to {}.'.format(
        source_file_name_1,
        destination_blob_name_1))
    
    print('File {} uploaded to {}.'.format(
        source_file_name_2,
        destination_blob_name_2))
    
upload_blob(bucket_name, source_file_name_1, source_file_name_2, destination_blob_name_1, destination_blob_name_2)