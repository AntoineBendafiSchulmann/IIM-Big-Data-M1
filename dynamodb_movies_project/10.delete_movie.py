import boto3

def delete_movie(movie_id, release_year):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.delete_item(
        Key={
            'movie_id': movie_id,
            'release_year': release_year
        }
    )
    return response

if __name__ == '__main__':
    print(delete_movie('uuid-2', 1999))
