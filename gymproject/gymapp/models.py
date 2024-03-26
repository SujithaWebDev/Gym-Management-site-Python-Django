from django.db import models

# Create your models here.
class Item(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    subscription=models.CharField(max_length=30, choices=(('No Subscription', 'No Subscription'), ('3 months', '3 months'), ('6 months', '6 months'), ('9 months', '9 months'), ('1 Year', '1 Year')))
    date=models.DateField(max_length=8)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    # description=models.TextField()

    def __str__(self):
        return self.name