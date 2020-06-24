from django.db import models

# Create your models here.
class Allproduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_cost = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
    