from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import User
from talaba.models import Talaba_activ
from arm.models import Bolim, Toifa
from arm.views import Yangiliklar
from dekanat.models import Fakultet, Kafedra, Yonalish, Kurs, Guruh, Lavozim

@csrf_exempt
def kirish(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.save()
            return redirect('/')
        else:
            messages.warning(request, 'xato')
            return redirect('/kirish')

    return render(request, 'superuser/admin/kirish.html')

@csrf_exempt
def home(request):
    talaaba_data = Talaba_activ.objects.all()
    yangilik = Yangiliklar.objects.all()      
    page = Paginator(yangilik, 3) 
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page' : page, 
        'talaba_data':talaaba_data,      
    }

    return render(request, 'asosiy/home.html', context)


@csrf_exempt
def dekanat(request):
    fakultetlar = Fakultet.objects.all()
    kafedralar = Kafedra.objects.all()
    lavozimlar = Lavozim.objects.all()
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']
        sharif = request.POST['sharif']
        viloyat = request.POST['viloyat']
        shahar = request.POST['shahar']
        kocha = request.POST['kocha']
        uy_nomer = request.POST['uy_nomer']
        email = request.POST['email']
        telefon = request.POST['telefon']               
        dekanat_fakultet = request.POST['dekanat_fakultet']
        dekanat_kafaedra = request.POST['dekanat_kafaedra']
        dekanat_lavozim = request.POST['dekanat_lavozim']       
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday ID mavjud'
        elif len(telefon) < 9:
            habar = 'Telefon nomerni kodi bilan kiriting'
        elif User.objects.filter(telefon=telefon):
            habar = 'Bumday telefon nomer mavjud'
        elif len(password1) < 8 or password1 == familya or password1 == ism:
            habar = 'Parol 8 tadan kam bolmasligi kerak'
        elif password1 != password2:
            habar = 'Tasdiqlash parolini to`gri kiritish'
        else:                                
            user = get_user_model().objects.create(lavozim = 'dekanat', username = username, email = email, last_name = familya, first_name = ism, password=make_password(password1), sharif=sharif, viloyat = viloyat, shahar = shahar, kocha = kocha, uy_nomer = uy_nomer, telefon = telefon, dekanat_lavozim =dekanat_lavozim, dekanat_kafaedra = dekanat_kafaedra, dekanat_fakultet = dekanat_fakultet,  parol= password2)
            user.is_active = False
            user.is_staff = False
            return redirect('/kirish')
        
    contex = {
        'habar' : habar,
        'fakultetlar' : fakultetlar,
        'kafedralar' : kafedralar,
        'lavozimlar' : lavozimlar,
    }    
    return render(request, 'superuser/admin/dekanat.html', contex)

@csrf_exempt
def arm(request):    
    bolimlar = Bolim.objects.all()
    toifalar = Toifa.objects.all()
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']
        sharif = request.POST['sharif']
        viloyat = request.POST['viloyat']
        shahar = request.POST['shahar']
        kocha = request.POST['kocha']
        uy_nomer = request.POST['uy_nomer']
        email = request.POST['email']
        telefon = request.POST['telefon']        
        arm_bolim = request.POST['arm_bolim']
        arm_toifa = request.POST['arm_toifa']        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday ID mavjud'
        elif len(telefon) < 9:
            habar = 'Telefon nomerni kodi bilan kiriting'
        elif User.objects.filter(telefon=telefon):
            habar = 'Bumday telefon nomer mavjud'
        elif len(password1) < 8 or password1 == familya or password1 == ism:
            habar = 'Parol 8 tadan kam bolmasligi kerak'
        elif password1 != password2:
            habar = 'Tasdiqlash parolini to`gri kiritish'
        else:                                
            user = get_user_model().objects.create(lavozim = 'arm', username = username, email = email, last_name = familya, first_name = ism, password=make_password(password1), sharif=sharif, viloyat = viloyat, shahar = shahar, kocha = kocha, uy_nomer = uy_nomer, telefon = telefon, arm_toifa = arm_toifa, arm_bolim = arm_bolim,  parol= password2)
            user.is_active = False
            user.is_staff = False
            return redirect('/kirish')
        
    contex = {
        'habar' : habar,
        'bolimlar' : bolimlar,
        'toifalar' : toifalar,
    }    
    return render(request, 'superuser/admin/arm.html', contex)

@csrf_exempt
def talaba(request):
    fakultetlar = Fakultet.objects.all()
    yonalishlar = Yonalish.objects.all()
    kurslar = Kurs.objects.all()
    guruhlar = Guruh.objects.all()
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']
        sharif = request.POST['sharif']
        viloyat = request.POST['viloyat']
        shahar = request.POST['shahar']
        kocha = request.POST['kocha']
        uy_nomer = request.POST['uy_nomer']
        email = request.POST['email']
        telefon = request.POST['telefon']      
        talaba_fakultet = request.POST['talaba_fakultet']
        talaba_yonalish = request.POST['talaba_yonalish']
        talaba_kurs = request.POST['talaba_kurs']
        talaba_guruh = request.POST['talaba_guruh']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday ID mavjud'
        elif len(telefon) < 9:
            habar = 'Telefon nomerni kodi bilan kiriting'
        elif User.objects.filter(telefon=telefon):
            habar = 'Bumday telefon nomer mavjud'
        elif len(password1) < 8 or password1 == familya or password1 == ism:
            habar = 'Parol 8 tadan kam bolmasligi kerak'
        elif password1 != password2:
            habar = 'Tasdiqlash parolini to`gri kiritish'
        else:                                
            user = get_user_model().objects.create(lavozim = 'talaba', username = username, email = email, last_name = familya, first_name = ism, password=make_password(password1), sharif=sharif, viloyat = viloyat, shahar = shahar, kocha = kocha, uy_nomer = uy_nomer, telefon = telefon, talaba_guruh = talaba_guruh, talaba_yonalish = talaba_yonalish, talaba_kurs = talaba_kurs, talaba_fakultet =talaba_fakultet,  parol= password2)
            user.is_active = False
            user.is_staff = False            
            return redirect('/kirish')
        
    contex = {
        'habar' : habar,
        'fakultetlar' : fakultetlar,
        'yonalishlar' : yonalishlar,
        'kurslar' : kurslar,
        'guruhlar' : guruhlar,
    }    
    return render(request, 'superuser/admin/talaba.html', contex)

@csrf_exempt
def superadmin(request):    
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']
        sharif = request.POST['sharif']
        viloyat = request.POST['viloyat']
        shahar = request.POST['shahar']
        kocha = request.POST['kocha']
        uy_nomer = request.POST['uy_nomer']
        email = request.POST['email']
        telefon = request.POST['telefon']       
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday ID mavjud'
        elif len(telefon) < 9:
            habar = 'Telefon nomerni kodi bilan kiriting'
        elif User.objects.filter(telefon=telefon):
            habar = 'Bumday telefon nomer mavjud'
        elif len(password1) < 8 or password1 == familya or password1 == ism:
            habar = 'Parol 8 tadan kam bolmasligi kerak'
        elif password1 != password2:
            habar = 'Tasdiqlash parolini to`gri kiritish'
        else:                                
            user = get_user_model().objects.create(lavozim = 'superadmin', username = username, email = email, last_name = familya, first_name = ism, password=make_password(password1), sharif=sharif, viloyat = viloyat, shahar = shahar, kocha = kocha, uy_nomer = uy_nomer, telefon = telefon,  parol= password2)
            user.is_active = False
            user.is_staff = False            
            return redirect('/kirish')
        
    contex = {
        'habar' : habar,        
    }    
    return render(request, 'superuser/admin/superadmin.html', contex)

@csrf_exempt
def adminlar(request):
    return render(request, 'superuser/admin/adminlar.html')

@csrf_exempt
def armadmin(request):
    return render(request, 'superuser/arm/armadmin.html')

@csrf_exempt
def dekanatadmin(request):
    return render(request, 'superuser/dekanat/dekanatadmin.html')

@csrf_exempt
def talabaadmin(request):
    return render(request, 'superuser/talaba/talaba.html')


@csrf_exempt
def superadmin_yangi(request):
    adminlar = get_user_model().objects.all()
    contex = {
        'adminlar' : adminlar,
    }
    return render(request, 'superuser/superadmin/superadmin_yangi.html', contex)

@csrf_exempt
def dekanat_yangi(request):
    adminlar = get_user_model().objects.all()
    contex = {
        'adminlar':adminlar,
    }
    return render(request, 'superuser/dekanat/dekanat_yangi.html', contex)

@csrf_exempt
def arm_yangi(request):
    adminlar = get_user_model().objects.all()
    contex = {
        'adminlar' : adminlar,
    }
    return render(request, 'superuser/arm/arm_yangi.html', contex)

