from django.db import models

# Create your models here.
class Allproduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_cost = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name

class UserAuth(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
    