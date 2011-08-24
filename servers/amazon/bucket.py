import boto
from boto.s3.connection import S3Connection, Location
from settings import AWS_KEY, AWS_SECRET_KEY

class Bucket(object):
    
    def __init__(self):
        self.conn = boto.connect_s3(AWS_KEY, AWS_SECRET_KEY)
        
    def create_bucket(self, bucket, location=Location.DEFAULT):
        self.conn.create_bucket(bucket, location=location)
        return
    
    def list_buckets(self):
        return self.conn.get_all_buckets()