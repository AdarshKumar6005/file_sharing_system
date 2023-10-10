from django.db import models
from django.conf import settings

# Create your models here.
class Files(models.Model):
    filename = models.CharField(max_length=100)
    date_uploaded = models.DateField()
    file = models.FileField(upload_to=settings.UPLOAD_FOLDER, default=None)