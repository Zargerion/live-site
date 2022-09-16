from django.db import models


class Creation(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pictures')
    link = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
