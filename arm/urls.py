from django.urls import path
from .views import yangi_kitob, kitoblar, talabalar, yangi_talaba, yangi_yangilik, yangiliklar
from .views import yangi_til, yangi_alfabit, yangi_resurs_sohasi, yangi_resurs_turi


urlpatterns = [ 
    path('kitoblar/', kitoblar, name='kitoblar'),
    path('yangi_kitob/', yangi_kitob, name='yangi_kitob'),
    path('talabalar/', talabalar, name='talabalar'), 
    path('yangi_talaba/', yangi_talaba, name='yangi_talaba'),  
    path('yangi_yangilik/', yangi_yangilik, name='yangi_yangilik'),
    path('yangiliklar/', yangiliklar, name='yangiliklar'), 
    path('yangi_til/', yangi_til, name='yangi_til'),
    path('yangi_alfabit/', yangi_alfabit, name='yangi_alfabit'),
    path('yangi_resurs_turi/', yangi_resurs_turi, name='yangi_resurs_turi'),
    path('yangi_resurs_sohasi/', yangi_resurs_sohasi, name='yangi_resurs_sohasi'),
]