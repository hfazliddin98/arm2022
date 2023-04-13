from django.db import models



class Lavozim(models.Model):
    lavozim = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lavozim
    

class Fakultet(models.Model):
    fakultet = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fakultet
    
    
class Kafedra(models.Model):
    kafedra = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kafedra
   
    
class Yonalish(models.Model):
    yonalish = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.yonalish
    
class Kurs(models.Model):
    kurs = models.CharField(max_length=10)
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.kurs
    
class Guruh(models.Model):
    guruh = models.CharField(max_length=10)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guruh