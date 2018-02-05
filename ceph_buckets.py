import sys
import os
import json
import boto3

s3 = None

def get_connected(profile='default', host='localhost', creds='/path/2/file'):
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = creds
    session = boto3.Session(profile_name=profile)
    s3 = session.client('s3', endpoint_url=host)
    return s3


def get_buckets(bucket_name=None):
    response = s3.list_buckets(Bucket=bucket_name)
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Bucket List: %s" % buckets)
    return buckets

def make_bucket(bucket_name):
    return s3.create_bucket(Bucket=bucket_name)

def upload(filename):
    key = os.path.basename(filename)
    s3.upload_file(filename, bucket_name, key)

def list_contents(bucket_name):
    print(json.dumps(s3.list_objects(Bucket=bucket_name)['Contents'], indent=4, default=str))

def show_acl(bucket_name):
    print(json.dumps(s3.get_bucket_acl(Bucket=bucket_name), indent=4))


def add_public_read():
    # Create the bucket policy
    bucket_policy = {
        #'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': "arn:aws:s3:::%s/*" % bucket_name
        }]
    }

    # Convert the policy to a JSON string
    bucket_policy = json.dumps(bucket_policy)

    # Set the new policy on the given bucket
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

def delete_file(bucket_name, key):
    s3.delete_object(Bucket=bucket_name, Key=key)

def delete_bucket(bucket_name):
    s3.delete_bucket(Bucket=bucket_name)

if __name__ == '__main__':
    host, creds, bucket_name = sys.argv[1:]
    s3 = get_connected(host=host, creds=creds)
    list_contents(bucket_name)

