from django.db import models

# Create your models here.
class Seller(models.Model):
    email = models.EmailField( max_length=100)
    usertype = models.CharField( max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.email
