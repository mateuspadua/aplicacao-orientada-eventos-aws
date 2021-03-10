import boto3
import json
import random

client = boto3.client("sns")

AWS_KEY_ID = "AKIA5AHNVOVVKLM7MLV6"
AWS_SECRET = "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"
TOPIC_ARN = "arn:aws:sns:us-east-1:893851628906:order"

sns = boto3.client(
    "sns",
    region_name="us-east-1",
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET,
)

sns.publish(
    TopicArn=TOPIC_ARN,
    Subject="some subject",
    Message=json.dumps({
        "customer": {
            "name": "Fulano de tal",
            "age": random.randint(1, 1000)
        },
        "amount": 15.0,
    }),
)

# print(sns.list_topics())
# print(sns.list_subscriptions())