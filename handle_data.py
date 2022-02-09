'''Read base data from Azure blob, 
add column to it and write to output container.'''

from os import environ
from dotenv import load_dotenv
import pandas as pd
from azure.storage.blob import ContainerClient

load_dotenv()

# Read base data via blob sas url
course_feedback = pd.read_csv(environ.get('URL_TO_INPUT_BLOB'))

# Create overall grade column
course_feedback['Overall'] = course_feedback.iloc[:, 4:7].mean(axis=1).round(2)

# Write new dataframe to csv locally
LOCAL_FILEPATH = '/usr/src/handle_data/data/course_feedback_finished.csv'
course_feedback.to_csv(LOCAL_FILEPATH, encoding='utf-8', index=False)

#Write local csv to Azure blob
cont_cli = ContainerClient.from_container_url(environ.get('URL_TO_OUTPUT_CONTAINER'))
with open(LOCAL_FILEPATH, 'rb') as data:
    cont_cli.upload_blob('coursedata-wrangled.csv', data, overwrite=True)
