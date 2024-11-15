import boto3

client = boto3.client('ecr')

repository_name = 'my-cloud-native-repo'
response = client.create_repository(repositoryName=repository_name) 

repositoty_uri = response['repository']['repositoryUri']
print(repositoty_uri)