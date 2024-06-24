import boto3
from decimal import Decimal

def add_awards_to_movie(movie_id, release_year, awards):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'movie_id': movie_id,
            'release_year': release_year
        },
        UpdateExpression="set details.awards = :a",
        ExpressionAttributeValues={
            ':a': awards
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    print(add_awards_to_movie('uuid-1', 2010, {'oscars': 4}))
