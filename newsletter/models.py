from django.db import models

class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient_list = models.TextField(help_text="Comma-separated emails")
    scheduled_time = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
