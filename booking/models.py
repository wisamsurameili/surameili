from django.db import models

# Create your models here.
class CarTires(models.Model):
    name = models.CharField(max_length=200 , verbose_name="Nimi")
    sureName = models.CharField(max_length=200 , verbose_name="Sukunimi" , null=True, blank=True)
    carNo = models.CharField(max_length=200 , verbose_name="Re. Numero" , null=True, blank=True)
    phoneNumber = models.CharField(max_length=200 , verbose_name="Puh. Numero" , null=True, blank=True)
    note = models.CharField(max_length=200 , verbose_name="Lisä tiedot" , null=True, blank=True)
    
    
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name_plural = "Car Tires"
        verbose_name = "Re."