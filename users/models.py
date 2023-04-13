from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    sharif = models.CharField(max_length=100)
    viloyat = models.CharField(max_length=200)
    shahar = models.CharField(max_length=200)
    kocha = models.CharField(max_length=200)
    uy_nomer = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)    
    parol = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)   
    # dekanat
    dekanat_fakultet = models.CharField(max_length=100, blank=True)
    dekanat_kafaedra = models.CharField(max_length=100, blank=True)
    dekanat_lavozim = models.CharField(max_length=100, blank=True)
    # arm
    arm_bolim = models.CharField(max_length=100, blank=True)
    arm_toifa = models.CharField(max_length=100, blank=True)
    # talaba
    talaba_fakultet = models.CharField(max_length=100, blank=True)
    talaba_yonalish = models.CharField(max_length=100, blank=True)
    talaba_kurs = models.CharField(max_length=100, blank=True)
    talaba_guruh = models.CharField(max_length=100, blank=True)



