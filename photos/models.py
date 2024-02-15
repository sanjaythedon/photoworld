from django.db import models


class Photos(models.Model):
    filepath = models.FileField(upload_to='img/')
    uploaded_by = models.CharField(max_length=50)
    