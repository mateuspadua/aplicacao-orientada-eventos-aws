import boto3
import json
import random

client = boto3.client("sns")

AWS_KEY_ID = "<sua AWS_KEY_ID>"
AWS_SECRET = "<seu AWS_SECRET>"
TOPIC_ARN = "arn:aws:sns:us-east-1:xxxxxxxxxxxxxx:order"

sns = boto3.client(
    "sns",
    region_name="us-east-1",
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET,
)

sns.publish(
    TopicArn=TOPIC_ARN,
    Subject="some subject",
    Message=json.dumps(
        {
            "customer": {"name": "Fulano de tal", "age": random.randint(1, 1000)},
            "amount": 15.0,
        }
    ),
)

# print(sns.list_topics())
# print(sns.list_subscriptions())