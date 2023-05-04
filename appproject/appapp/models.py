from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    details = models.TextField()
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    def __str__(self):
        return self.name