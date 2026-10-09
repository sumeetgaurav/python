"""Uploads a local file to an AWS S3 bucket using boto3."""

import boto3

s3 = boto3.resource('s3')

file_name = r"C:\dev-ops\ai-powered\python\fde-devops\day1\api.py"
object_name = "api.py"
bucket_name = "devops-fde"

s3.Bucket(bucket_name).upload_file(file_name, object_name)
print("Upload complete")