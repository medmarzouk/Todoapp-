from django.db import models

# Create your models here.
class Apps(models.Model):
    title = models.CharField(max_length=200, null=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    Created_at = models.DateTimeField(auto_now_add=True)