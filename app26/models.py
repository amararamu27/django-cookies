from django.db import models

class ProductModel(models.Model):
    pno = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    images = models.ImageField(upload_to='product_images/')
    features = models.TextField(blank=True)
