from django.db import models




class Yangiliklar(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    rasm = models.FileField(upload_to='yangiliklar/')                
    sana = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.title
        
class Kitoblar(models.Model):
    shifr = models.CharField(max_length=200)
    aftor_belgisi = models.CharField(max_length=200)
    invertor_nomeri = models.CharField(max_length=200)
    mualiflar = models.CharField(max_length=200)
    kitob_nomi = models.CharField(max_length=200)
    nashriyot = models.CharField(max_length=200)
    nashr_yili = models.CharField(max_length=200)  
    isbn = models.CharField(max_length=200)
    kitob_narxi = models.CharField(max_length=200)
    tili = models.CharField(max_length=200)
    alfabit = models.CharField(max_length=200)
    darslik_turi = models.CharField(max_length=200)
    kitobni_fondagi_soni =  models.CharField(max_length=200)
    anatatsiya = models.CharField(max_length=10000)
    mundarija = models.CharField(max_length=600, blank=True)
    kitob_turi = models.CharField(max_length=100)
    kitob_rasmi= models.FileField(upload_to='rasm/', blank=True)
    fayl = models.FileField(upload_to='kitob/', blank=True)
    sana = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.kitob_nomi


class Talabalar(models.Model):
    talaba_id = models.CharField(max_length=100)
    invertor_nomeri = models.CharField(max_length=100)
    formulyar_raqami = models.CharField(max_length=200)     
    tel_raqami = models.CharField(max_length=200)
    pasport_seryasi = models.CharField(max_length=200)
    pasport_raqami = models.CharField(max_length=200)
    sana = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.formulyar_raqami

class Bolim(models.Model):
    bolim = models.CharField(max_length=200)

    def __str__(self):
        return self.bolim
    
class Toifa(models.Model):
    toifa = models.CharField(max_length=200)

    def __str__(self):
        return self.toifa
    

class Tili(models.Model):
    tili = models.CharField(max_length=100)

    def __str__(self):
        return self.tili
    
class Alfabit(models.Model):
    alfabit = models.CharField(max_length=100)

    def __str__(self):
        return self.alfabit
    
class Resurs_sohasi(models.Model):
    resurs_sohasi = models.CharField(max_length=100)

    def __str__(self):
        return self.resurs_sohasi
    
class Resurs_turi(models.Model):
    resurs_turi = models.CharField(max_length=100)

    def __str__(self):
        return self.resurs_turi