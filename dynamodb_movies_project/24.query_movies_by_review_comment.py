import boto3
from boto3.dynamodb.conditions import Attr

def query_movies_by_review_comment(keyword):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan(
        FilterExpression=Attr('details.reviews[0].comment').contains(keyword) | 
        Attr('details.reviews[1].comment').contains(keyword)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_movies_by_review_comment('Amazing'))
