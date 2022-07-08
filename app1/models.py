from django.db import models

# Create your models here.


class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    heading=models.CharField(max_length=16)
    Category=models.CharField(max_length=16)
    tags=models.CharField(max_length=16)
    content=models.TextField()
    