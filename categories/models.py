from email.policy import default
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories', default="")

    def __str__(self):
        return self.title
