from socket import fromshare
from django.db import models

# Create your models here.

class AudioFile(models.Model):
    record=models.FileField()
    class Meta:
        db_table='AudioFile'
