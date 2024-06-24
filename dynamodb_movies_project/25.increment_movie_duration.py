import boto3
from decimal import Decimal

def increment_movie_duration(movie_id, release_year, increment):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'movie_id': movie_id,
            'release_year': release_year
        },
        UpdateExpression="set details.duration = details.duration + :inc",
        ExpressionAttributeValues={
            ':inc': Decimal(str(increment))
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    print(increment_movie_duration('uuid-1', 2010, 10))
