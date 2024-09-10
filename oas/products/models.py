from django.db import models

class products(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(max_length=200, upload_to="products/", null=True)


# Create your models here.
