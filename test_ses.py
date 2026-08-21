import boto3
import os
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION")

ses = boto3.client("ses", region_name=region)

sender = "nyamanyunzotanaka@gmail.com"
recipient = "nyamanyunzotanaka@gmail.com"

response = ses.send_email(
    Source=sender,
    Destination={
        "ToAddresses": [
            recipient
        ]
    },
    Message={
        "Subject": {
            "Data": "Medication Reminder Test"
        },
        "Body": {
            "Text": {
                "Data": "This is a test email from the Medication Reminder Service."
            }
        }
    }
)

print("Email sent successfully")
print("Message ID:", response["MessageId"])