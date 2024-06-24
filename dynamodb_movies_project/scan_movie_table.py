import boto3

def scan_movies_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Movies')

    response = table.scan()
    items = response['Items']

    for item in items:
        print(item)

if __name__ == '__main__':
    scan_movies_table()
