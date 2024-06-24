import boto3

def count_movies():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan()
    return response['Count']

if __name__ == '__main__':
    print(f"Total number of movies: {count_movies()}")
