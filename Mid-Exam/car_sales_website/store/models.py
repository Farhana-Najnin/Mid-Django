from django.db import models
from category.models import Brand
from django.contrib.auth.models import User 
# Create your models here.

class Car(models.Model):
    carName = models.CharField(max_length=50)
    carPrice = models.DecimalField(max_digits= 10, decimal_places=2)
    quantity = models.IntegerField(default=5)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to ='store/media/uploads/', blank=True, null=True)

    def __str__(self):
        return self.carName
    
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete = models.CASCADE, related_name = "comments")
    name =  models.CharField(max_length = 50)
    email  = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"comment by{self.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.car.carName}"