import boto3
from boto3.dynamodb.conditions import Attr

def query_movies_after_year(year):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('release_year').gt(year)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_after_year(2000))
