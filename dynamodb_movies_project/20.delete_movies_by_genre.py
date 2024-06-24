import boto3
from boto3.dynamodb.conditions import Key

def delete_movies_by_genre(genre):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.query(
        IndexName='GenreIndex',
        KeyConditionExpression=Key('genre').eq(genre)
    )
    items = response['Items']

    with table.batch_writer() as batch:
        for item in items:
            batch.delete_item(
                Key={
                    'movie_id': item['movie_id'],
                    'release_year': item['release_year']
                }
            )

if __name__ == '__main__':
    delete_movies_by_genre('Action')
    print("Movies of genre 'Action' deleted.")
