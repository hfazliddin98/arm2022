from django.db import models
from users.models import User
from arm.models import Talabalar, Kitoblar


class Viloyat(models.Model):
    viloyat = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.viloyat
    
class Tuman(models.Model):
    tuman = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tuman 
    

class Mfy(models.Model):
    mfy = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.mfy   
    
class Talaba(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    talabalat_id = models.ForeignKey(Talabalar, on_delete=models.CASCADE)
    kitoblar_id = models.ForeignKey(Kitoblar, on_delete=models.CASCADE)

    def __str__ (self):
        return self.user_id.username
    
class Sinov(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)

    def __str__(self):
        return self.ism


 

