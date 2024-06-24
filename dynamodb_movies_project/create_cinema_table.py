import boto3
import time
from botocore.exceptions import ClientError

def create_cinema_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    try:
        table = dynamodb.create_table(
            TableName='Cinema',
            KeySchema=[
                {'AttributeName': 'cinema_id', 'KeyType': 'HASH'}, 
                {'AttributeName': 'movie_id', 'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'cinema_id', 'AttributeType': 'S'},
                {'AttributeName': 'movie_id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("Table already exists. Skipping creation.")
        else:
            raise

def wait_for_table_active(table_name):
    dynamodb = boto3.client('dynamodb', region_name='us-west-2')
    while True:
        response = dynamodb.describe_table(TableName=table_name)
        status = response['Table']['TableStatus']
        if status == 'ACTIVE':
            break
        time.sleep(5)
    print(f"Table {table_name} is now ACTIVE.")

if __name__ == '__main__':
    table = create_cinema_table()
    if table:
        print(f"Table status: {table.table_status}")
        wait_for_table_active('Cinema')
