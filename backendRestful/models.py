from django.db import models
from versatileimagefield.fields import VersatileImageField

class Allproduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_cost = models.CharField(max_length=200)

    image = VersatileImageField(
        upload_to='images/testimagemodel/',
        blank=True,
        null = True
    )
    product_type = models.CharField(max_length=125,null=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    # image = models.ImageField(upload_to = 'image/%Y/%m/%d', null= True, blank= True)
