from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Orderuser(models.Model):
    order_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(max_length=10, blank=True, null=True)
    telephone_number = models.CharField(max_length=10, blank=True, null=True)
    total_cost = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.order_id} {0.author} {0.first_name} {0.last_name} {0.total_cost} {0.telephone_number}'
        return template.format(self)


class Productinorder(models.Model):
    product_name = models.CharField(max_length=255, null=True)
    product_cost = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    quantity = models.CharField(max_length=1000, null=True)
    order = models.ForeignKey(Orderuser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        template = '{0.product_name} {0.quantity} {0.image} {0.order}'
        return template.format(self)
