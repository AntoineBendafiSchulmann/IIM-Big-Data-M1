import boto3

def add_reviews_to_movie(movie_id, release_year, reviews):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'movie_id': movie_id,
            'release_year': release_year
        },
        UpdateExpression="set details.reviews = :r",
        ExpressionAttributeValues={
            ':r': reviews
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    reviews = [
        {"reviewer": "John Doe", "comment": "Excellent!"},
        {"reviewer": "Jane Doe", "comment": "Amazing!"}
    ]
    print(add_reviews_to_movie('uuid-1', 2010, reviews))
