from django.db import models
from musician.models import Musician
# Create your models here.
class album(models.Model):
    albumName = models.CharField(max_length=30)
    albumReleaseDate = models.DateField()
    rating = models.IntegerField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.albumName