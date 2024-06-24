import boto3
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal

def query_movies_by_release_year_and_rating(year, rating):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.query(
        IndexName='ReleaseYearRatingIndex',
        KeyConditionExpression=Key('release_year').eq(year) & Key('rating').gt(Decimal(str(rating)))
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_release_year_and_rating(2014, 8.5))
