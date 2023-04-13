from django.urls import path
from .views import kirish, dekanat, arm, talaba, home, superadmin, armadmin, dekanatadmin, talabaadmin, adminlar
from .views import arm_yangi, dekanat_yangi, superadmin_yangi
urlpatterns = [    
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('user/dekanat/', dekanat, name='dekanat'),
    path('user/dekanat_yangi', dekanat_yangi, name='dekanat_yangi'),
    path('user/arm/', arm, name='arm'),
    path('user/arm_yangi/', arm_yangi, name='arm_yangi'),
    path('user/talaba/', talaba, name='talaba'), 
    path('user/adminlar/', adminlar, name='adminlar'),
    path('user/superadmin/', superadmin, name='superadmin'),
    path('user/superadmin_yangi/', superadmin_yangi, name='superadmin_yangi'),
    path('user/armadmin/', armadmin, name='armadmin'),
    path('user/dekanatadmin/', dekanatadmin, name='dekanatadmin'),   
    path('user/talabaadmin/', talabaadmin, name='talabaadmin'), 
]