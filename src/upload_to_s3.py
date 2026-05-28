import boto3
import os

BUCKET_NAME = "satellite-telemetry-rob-casey"
LOCAL_FILE = "data/tle_raw.json"
S3_KEY = "raw/tle_raw.json"

def upload_to_s3(local_file, bucket, s3_key): 
    s3 = boto3.client("s3")
    s3.upload_file(local_file, bucket, s3_key)
    print(f"Uploaded {local_file} to s3://{bucket}/{s3_key}")

if __name__ == "__main__":
    upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_KEY)