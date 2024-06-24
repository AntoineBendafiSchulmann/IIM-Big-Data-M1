import boto3
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal

def get_movie(movie_id, release_year):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.get_item(
        Key={
            'movie_id': movie_id,
            'release_year': release_year
        }
    )
    return response.get('Item')

def query_movies_by_genre(genre):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.query(
        IndexName='GenreIndex',
        KeyConditionExpression=Key('genre').eq(genre)
    )
    return response['Items']

def query_movies_after_year(year):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('release_year').gt(year)
    )
    return response['Items']

def query_movies_by_rating(rating):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('rating').gt(Decimal(str(rating)))
    )
    return response['Items']

if __name__ == '__main__':
    print(get_movie('uuid-1', 2010))
    print(query_movies_by_genre('Sci-Fi'))
    print(query_movies_after_year(2000))
    print(query_movies_by_rating(8.5))
