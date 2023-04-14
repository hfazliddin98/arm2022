from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
from dekanat.models import Fakultet
from users.models import User
from .models import Yangiliklar, Talabalar, Kitoblar

@csrf_exempt
def yangi_yangilik(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        rasm = request.POST['rasm']
        Yangiliklar.objects.create(title=title, body=body, rasm=rasm)        
        return redirect('/')
    return render(request, 'arm/arm_3/yangilik_kiritish.html')



@csrf_exempt
def talabalar(request):
    data = Talabalar.objects.all()   
    contex = {
        'data':data,
    }
    return render(request, 'arm/arm_2/talabalar.html', contex)


@csrf_exempt
def yangi_talaba(request):
    talaba_id = User.objects.all()
    invertor= Kitoblar.objects.all()
    if request.method == 'POST':
        talaba_id = request.POST['talaba_id']
        invertor_nomeri = request.POST['invertor_nomeri']
        formulyar_raqami = request.POST['formulyar_raqami']
        tel_raqami = request.POST['tel_raqami']
        pasport_seryasi = request.POST['pasport_seryasi']
        pasport_raqami = request.POST['pasport_raqami']        
        Talabalar.objects.create(talaba_id=talaba_id, invertor_nomeri=invertor_nomeri, formulyar_raqami=formulyar_raqami, tel_raqami=tel_raqami, pasport_seryasi=pasport_seryasi, pasport_raqami=pasport_raqami)
        return redirect('/')
    contex = {
        'talaba_id' : talaba_id,
        'invertor' : invertor,
    }
    return render(request, 'arm/arm_2/yangi_talaba.html', contex)



@csrf_exempt
def yangi_kitob(request):
    fakultet = Fakultet.objects.all()
    if request.method == 'POST':
        shifr = request.POST['shifr']
        aftor_belgisi = request.POST['aftor_belgisi']
        invertor_nomeri = request.POST['invertor_nomeri']
        mualiflar = request.POST['mualiflar']
        kitob_nomi = request.POST['kitob_nomi']
        nashriyot = request.POST['nashriyot']
        nashr_yili = request.POST['nashr_yili']
        isbn = request.POST['isbn']
        kitob_narxi = request.POST['kitob_narxi']
        tili = request.POST['tili']
        alfabit = request.POST['alfabit']
        darslik_turi = request.POST['darslik_turi']
        kitobni_fondagi_soni = request.POST['kitobni_fondagi_soni']
        anatatsiya = request.POST['anatatsiya']
        # mundarija = request.POST['mundarija']
        kitob_turi = request.POST['kitob_turi']
        kitob_rasmini_kiriting = request.POST['kitob_rasmini_kiriting']
        fayl = request.POST['fayl']
        Kitoblar.objects.create(mualiflar=mualiflar, fayl=fayl, kitob_rasmini_kiriting=kitob_rasmini_kiriting, kitob_turi=kitob_turi, anatatsiya=anatatsiya, kitobni_fondagi_soni=kitobni_fondagi_soni, darslik_turi=darslik_turi, alfabit=alfabit, tili=tili, kitob_narxi=kitob_narxi, isbn=isbn, nashr_yili=nashr_yili, nashriyot=nashriyot, kitob_nomi=kitob_nomi, shifr=shifr,aftor_belgisi=aftor_belgisi,invertor_nomeri=invertor_nomeri)
        return redirect('/')
    contex = {
        'fakultet':fakultet,
    }
    return render(request, 'arm/arm_1/yangi_kitob.html', contex)

@csrf_exempt
def kitoblar(request):
    data = Kitoblar.objects.all()
    contex  = {
        'data':data,
    }
    return render(request, 'arm/arm_1/kitoblar.html', contex)


@csrf_exempt
def yangiliklar(request):
    data = Yangiliklar.objects.all()
    contex = {
        'data':data,
    }
    return render(request, 'arm/arm_3/yangiliklar.html', contex)