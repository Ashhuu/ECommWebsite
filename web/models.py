from django.db import models

# Create your models here.

class ProductDetails(models.Model):
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=50)
    productDesc = models.TextField()
    productImage = models.ImageField(upload_to="image/")
    productPrice = models.IntegerField()