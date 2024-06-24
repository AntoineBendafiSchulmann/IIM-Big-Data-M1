import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Attr

def query_movies_by_rating(rating):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('rating').gt(Decimal(str(rating)))
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_rating(8.5))
