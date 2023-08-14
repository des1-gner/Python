import boto3
import sys
from botocore.exceptions import ClientError

filename = sys.argv[1] 

dest_bucket = "tim-jam-working-bucket"
data_dir = "data/"
prefix = "api_migration/"
s3_client = boto3.client('s3')

input_file = open(filename, 'r')
key_list = ["".join(line.split()) for line in input_file.readlines()]

for key in key_list:
    try:
        response = s3_client.upload_file(data_dir+key, dest_bucket, prefix+key)
        print('uploading - %s\n' % key)
    except ClientError as e:
        print('%s - %s\n' % key % e.response['Error']['Code'])