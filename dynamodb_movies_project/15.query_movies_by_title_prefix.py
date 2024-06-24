import boto3
from boto3.dynamodb.conditions import Attr

def query_movies_by_title_prefix(prefix):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('title').begins_with(prefix)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_title_prefix('I'))
