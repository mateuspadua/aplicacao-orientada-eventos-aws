import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns_client = boto3.client("sns")


def lambda_handler(event, context):

    message = json.loads(event["Records"][0]["Sns"]["Message"])

    # Envia a mensagem
    response = sns_client.publish(
        PhoneNumber=str(message["phone"]),
        Message="Oi! Esta é uma mensagem enviada com a Amazon SNS",
    )

    logger.info(response)
    return "OK"
