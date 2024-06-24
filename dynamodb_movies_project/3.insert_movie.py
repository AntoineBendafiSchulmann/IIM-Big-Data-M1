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

if __name__ == '__main__':
    insert_movie()
    print("Movie inserted.")
