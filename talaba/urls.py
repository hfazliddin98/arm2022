from django.urls import path
from .views import viloyat, tuman, mfy
from .views import talaba_kitob, sinov, update

urlpatterns = [ 
   path('talaba_kitob/', talaba_kitob, name='talaba_kitob'),
   path('', viloyat, name='viloyat'),
   path('tuman/', tuman, name='tuman'),
   path('mfy/', mfy, name='mfy'),
   path('sinov/', sinov, name='sinov'),
   path('update/<int:pk>/', update, name='update'),
]