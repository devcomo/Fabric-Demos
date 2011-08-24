import boto
import boto.ec2
from settings import AWS_KEY, AWS_SECRET_KEY

class Ec2(object):
    
    def __init__(self):
        self.conn = boto.connect_ec2(AWS_KEY, AWS_SECRET_KEY)

    def get_regions(self):
        return self.conn.regions()