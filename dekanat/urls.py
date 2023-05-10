from django.urls import path
from .views import fakultet, fakultetlar, kafedra
from .views import fakultet, yonalish, kurs, guruh

urlpatterns = [ 
   path('fakultet_yangi/', fakultet, name='fakultet_yangi'),  
   path('yonalish_yangi/', yonalish, name='yonalish_yangi'),
   path('kurs_yangi/', kurs, name='kurs_yangi'),
   path('guruh_yangi/', guruh, name='guruh_yangi'),
   path('fakultetlar/', fakultetlar, name='fakultetlar'),
   path('kafedra/', kafedra, name='kafedra'),
]