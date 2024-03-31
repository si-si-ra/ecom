from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    # image=models.CharField(max_length=2000)

    # created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

# Create your models here.
