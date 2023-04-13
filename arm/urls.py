from django.urls import path
from .views import yangi_kitob, kitoblar, talabalar, yangi_talaba, yangi_yangilik, yangiliklar


urlpatterns = [ 
    path('kitoblar/', kitoblar, name='kitoblar'),
    path('yangi_kitob/', yangi_kitob, name='yangi_kitob'),
    path('talabalar/', talabalar, name='talabalar'), 
    path('yangi_talaba/', yangi_talaba, name='yangi_talaba'),  
    path('yangi_yangilik/', yangi_yangilik, name='yangi_yangilik'),
    path('yangiliklar/', yangiliklar, name='yangiliklar'), 
]