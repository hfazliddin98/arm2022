from django.contrib import admin
from .models import Fakultet, Kafedra ,Yonalish, Kurs, Guruh,Lavozim

admin.site.register([Fakultet, Kafedra, Yonalish, Kurs, Guruh, Lavozim])