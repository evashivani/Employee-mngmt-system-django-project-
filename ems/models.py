from django.db import models


# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)
    year_of_exp=models.IntegerField()
    contact=models.CharField(max_length=20)
    def __str__(self):
        return self.name
