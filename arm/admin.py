from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Yangiliklar, Kitoblar, Talabalar, Bolim, Toifa
from .models import Tili, Alfabit, Resurs_sohasi, Resurs_turi

admin.site.unregister(Group)
admin.site.register([Yangiliklar, Kitoblar, Talabalar, Bolim, Toifa])
admin.site.register([Tili, Alfabit, Resurs_sohasi, Resurs_turi])
