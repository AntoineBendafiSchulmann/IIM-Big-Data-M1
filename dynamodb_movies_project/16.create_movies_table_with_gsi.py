import boto3
from botocore.exceptions import ClientError

def create_movies_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    try:
        table = dynamodb.create_table(
            TableName='Movies',
            KeySchema=[
                {'AttributeName': 'movie_id', 'KeyType': 'HASH'},
                {'AttributeName': 'release_year', 'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'movie_id', 'AttributeType': 'S'},
                {'AttributeName': 'release_year', 'AttributeType': 'N'},
                {'AttributeName': 'genre', 'AttributeType': 'S'},
                {'AttributeName': 'rating', 'AttributeType': 'N'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            },
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GenreIndex',
                    'KeySchema': [
                        {'AttributeName': 'genre', 'KeyType': 'HASH'}
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                    }
                },
                {
                    'IndexName': 'ReleaseYearRatingIndex',
                    'KeySchema': [
                        {'AttributeName': 'release_year', 'KeyType': 'HASH'},
                        {'AttributeName': 'rating', 'KeyType': 'RANGE'}
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                    }
                }
            ]
        )
        return table
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("Table already exists. Skipping creation.")
        else:
            raise

if __name__ == '__main__':
    table = create_movies_table()
    if table:
        print(f"Table status: {table.table_status}")
