import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    # TODO implement

    s3 = boto3.client("s3")

    body = json.loads(event["Records"][0]["body"])
    message = body["Message"]

    s3.put_object(
        Body=message,
        Bucket="seu_bucket",
        Key=f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.txt",
    )

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
