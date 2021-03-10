import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    print(type(event))
    data = json.loads(event["Records"][0]["body"])
    message = json.loads(data["Message"])
    print("******")
    print(data)
    s3.put_object(Bucket="tutoriais-mateus", Key=f"{datetime.now().timestamp()}.json", Body=json.dumps(message))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }