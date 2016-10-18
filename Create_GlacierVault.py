### Code to create AWS Glacier Vault
### IAM must be setup to allow correct writing privileges to AWS Glacier
### Be sure that credentials are downloaded to local root

### SDK to connect to AWS Glacier
import boto3
import argparse

### Calls credentials in local root
from botocore.client import Config

### Pull arguments from command line
argparser = argparse.ArgumentParser()
argparser.add_argument("vaultname")

vaultname = args.vaultname

### Assign client AWS Glacier Storage
client = boto3.client('glacier')


### Create a New Vault, with printed response
response = client.create_vault(
    vaultName=vaultName
)

print(response)
