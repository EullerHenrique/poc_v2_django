from django.db import models

class Token(models.Model):
    access_token = models.CharField(max_length=255, primary_key=True)
    expires_in = models.IntegerField()
    expires_at = models.DateTimeField()
