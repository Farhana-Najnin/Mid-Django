from django.db import models

# Create your models here.
class Brand(models.Model):
    brandName = models.CharField(max_length=60)
    slug = models.SlugField(max_length = 100,unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.brandName