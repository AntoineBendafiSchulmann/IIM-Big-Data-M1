import boto3
from boto3.dynamodb.conditions import Key

def query_movies_by_release_year(year):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.query(
        IndexName='ReleaseYearRatingIndex',
        KeyConditionExpression=Key('release_year').eq(year)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_release_year(2014))
