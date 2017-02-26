### Code to upload files to S3
### Code will overwite colliding files
### IAM must be setup to allow correct writing privileges to S3
### Be sure that credentials are downloaded to local root

### SDK to connect to AWS Glacier
import boto3
import argparse

### Calls credentials in local root
from botocore.client import Config

### Pull arguments from command line
argparser = argparse.ArgumentParser()
argparser.add_argument("srcPath")

vaultname = args.vaultname

### Assign client AWS S3
client = boto3.client('s3')

### Upload File to S3 Path -- For Now bucket/path exists, will eventually
### create code to create a new bucket/path when it does not already exist.
