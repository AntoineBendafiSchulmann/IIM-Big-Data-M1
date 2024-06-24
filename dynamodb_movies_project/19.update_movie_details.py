import boto3

def update_movie_details(movie_id, release_year, new_details):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'movie_id': movie_id,
            'release_year': release_year
        },
        UpdateExpression="set details = :d",
        ExpressionAttributeValues={
            ':d': new_details
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    new_details = {'director': 'Wachowski', 'duration': 136, 'sequels': 2}
    print(update_movie_details('uuid-2', 1999, new_details))
