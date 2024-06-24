import boto3
from decimal import Decimal

def insert_movie():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    table.put_item(
        Item={
            'movie_id': 'uuid-1',
            'title': 'Inception',
            'release_year': 2010,
            'genre': 'Sci-Fi',
            'rating': Decimal('8.8'),
            'details': {'director': 'Christopher Nolan', 'duration': 148}
        }
    )

def insert_movies_batch():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'movie_id': 'uuid-2',
                'title': 'The Matrix',
                'release_year': 1999,
                'genre': 'Action',
                'rating': Decimal('8.7'),
                'details': {'director': 'Wachowski', 'duration': 136}
            }
        )
        batch.put_item(
            Item={
                'movie_id': 'uuid-3',
                'title': 'Interstellar',
                'release_year': 2014,
                'genre': 'Sci-Fi',
                'rating': Decimal('8.6'),
                'details': {'director': 'Christopher Nolan', 'duration': 169}
            }
        )

if __name__ == '__main__':
    insert_movie()
    insert_movies_batch()
    print("Movies inserted.")
