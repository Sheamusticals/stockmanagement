from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Item_Name =  models.CharField(max_length=200)
    Manufacturer = models.CharField(max_length=200)
    Price =  models.CharField(max_length=200)
    Quantity = models.IntegerField()
    Expiry_Date = models.DateField(null=True)
    Date_Issued = models.DateTimeField('date issued')

    def __str__(self):
        return self.Item_Name
       

    class Meta:
         
        ordering = ['Date_Issued'] 


    
