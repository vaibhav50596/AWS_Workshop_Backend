import json
import boto3
from pprint import pprint
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")


#documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.create_table
table = dynamodb.create_table(
    TableName='courses',
    KeySchema=[
        {
            'AttributeName': 'courseid',
            'KeyType': 'HASH'  #Partition key - organizes the items
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'courseid',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)