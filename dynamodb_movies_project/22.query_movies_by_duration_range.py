import boto3
from boto3.dynamodb.conditions import Attr

def query_movies_by_duration_range(min_duration, max_duration):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('details.duration').between(min_duration, max_duration)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_duration_range(120, 180))
