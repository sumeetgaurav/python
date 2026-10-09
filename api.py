"""FastAPI web service exposing endpoints for a health check, live system metrics, and AWS S3 bucket listing."""

from fastapi import FastAPI
from system_utils import get_system_info
import boto3

s3=boto3.resource('s3')
app = FastAPI(title="My API", description="This is my API", version="1.0.0")

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/metrics")
def metrics():

    """
    Get system metrics."""
    return get_system_info()

@app.get("/aws/s3/buckets")
def get_buckets():
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    return {"buckets": buckets}