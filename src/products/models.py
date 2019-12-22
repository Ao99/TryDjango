from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120); # has to use max_length
    description = models.TextField(blank=True, null=True);
    price = models.DecimalField(max_digits=1000, decimal_places=2);
    summary = models.TextField(blank=True,null=False);
    featured = models.BooleanField(); # 1.null = True 2.default=True 3.both
    
    def get_absolute_url(self):
        # method 1
        # return f'/product/{self.id}'
        # there must be a / in front of product, other wise it
        # will be treated as a relative url, such as product/product/3
        # method 2
        return reverse('products:product-detail', kwargs={"currId": self.id})
        # app_name:path-name in urls