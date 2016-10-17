### Code to create AWS Glacier Vault
### IAM must be setup to allow correct writing privileges to AWS Glacier
### Be sure that credentials are downloaded to local root

### SDK to connect to AWS Glacier
import boto3

### Calls credentials in local root
from botocore.client import Config

### Assign client AWS Glacier Storage
client = boto3.client('glacier')


### Create a New Vault, with printed repsonse
response = client.create_vault(
    vaultName='Akash_DW_TEST'
)

print(response)
