from django.db import models

# Create your models here.


class user_url(models.Model):
    url = models.CharField(max_length=100)
