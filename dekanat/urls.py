from django.urls import path
from .views import fakultet, fakultetlar, kafedra

urlpatterns = [ 
   path('', fakultet, name='fakultet'),    
   path('fakultetlar/', fakultetlar, name='fakultetlar'),
   path('kafedra/', kafedra, name='kafedra'),
]