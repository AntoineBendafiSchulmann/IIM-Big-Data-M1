import boto3
from boto3.dynamodb.conditions import Key

def query_movies_by_genre(genre):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.query(
        IndexName='GenreIndex',
        KeyConditionExpression=Key('genre').eq(genre)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_genre('Sci-Fi'))
