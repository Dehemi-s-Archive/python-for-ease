import boto3
import json

from botocore.client import Config 
# Read config
with open("../config.json","r") as config_file:
     config = json.load(config_file)

#Initialize
session = boto3.session.Session()
client = session.client('s3', region_name=config['region_name'], endpoint_url=config['endpoint_url'], aws_access_key_id=config['aws_access_key_id'], aws_secret_access_key=config['aws_secret_access_key'])

#New Space
#client.create_bucket(Bucket=config['bucket'])

#List all buckets
res = client.list_buckets()
#spaces = [space['Name'] for space in res['Buckets']]
#print("Spcaes List %s" % spaces)
print(res)
