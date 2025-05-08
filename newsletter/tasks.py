from celery import shared_task
import boto3
from django.utils.timezone import now
from .models import Newsletter

@shared_task
def send_scheduled_newsletters():
    newsletters = Newsletter.objects.filter(sent=False, scheduled_time__lte=now())
    ses = boto3.client('ses', region_name='us-east-1')

    for newsletter in newsletters:
        for email in newsletter.recipient_list.split(','):
            ses.send_email(
                Source='your_verified_email@example.com',
                Destination={'ToAddresses': [email.strip()]},
                Message={
                    'Subject': {'Data': newsletter.subject},
                    'Body': {'Text': {'Data': newsletter.body}}
                }
            )
        newsletter.sent = True
        newsletter.save()
