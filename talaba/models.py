from django.db import models


class Talaba_activ(models.Model):
    talaba_id = models.CharField(max_length=100)
    activ = models.CharField(max_length=100)

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

 

