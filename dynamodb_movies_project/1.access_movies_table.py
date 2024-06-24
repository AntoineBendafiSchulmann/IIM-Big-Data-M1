import boto3

def get_dynamodb_resource():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    return dynamodb

if __name__ == '__main__':
    dynamodb = get_dynamodb_resource()
    table = dynamodb.Table('Movies')
    print("Accessed table:", table.table_name)
