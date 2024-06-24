import boto3

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

if __name__ == '__main__':
    print(get_movie('uuid-1', 2010))
