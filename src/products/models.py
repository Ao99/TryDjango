from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120); # has to use max_length
    description = models.TextField(blank=True, null=True);
    price = models.DecimalField(max_digits=1000, decimal_places=2);
    summary = models.TextField(blank=True,null=False);
    featured = models.BooleanField(); # 1.null = True 2.default=True 3.both