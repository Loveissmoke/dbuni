from django.db import models
from colorfield.fields import ColorField
from cloudinary.models import CloudinaryField

class Brand(models.Model):
    name = models.CharField(max_length=100)
#    image = models.ImageField(upload_to='brands/')

    image = CloudinaryField('image')
    description = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gram = models.IntegerField()
    pieces_per_case = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    text_color = ColorField(default='#000000')
    bg_color = ColorField(default='#ffffff')
    def __str__(self):
        return f"{self.name} ({self.gram}g)"
