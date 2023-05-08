from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect
from users.models import User
from .models import  Viloyat, Tuman, Mfy, Talaba, Sinov
from arm.models import Kitoblar, Talabalar




@csrf_exempt
def talaba_kitob(request):
    talaba_id = request.user.id
    user = User.objects.get(id = talaba_id)
    data = Talabalar.objects.all
    talaba = Talaba.objects.all()   
 
    
    contex = {
        'talaba':talaba,
        'data':data,
        'user':user,
    }
    return render(request, 'talaba/kitoblar/kitoblar.html', contex)


@csrf_exempt
def viloyat(request):
    habar = ''
    if request.method == 'POST':
        viloyatlar = request.POST['viloyat']
        if Viloyat.objects.filter(viloyat=viloyatlar):
            habar = 'Bunday viloyat mavjud'
        else:
            baza = Viloyat.objects.create(viloyat=viloyatlar)
            baza.save()
        return redirect('/talaba')
    contex = {
        'habar' : habar,
    }
    return render(request, 'viloyat/viloyat.html', contex)


@csrf_exempt
def tuman(request):
    habar = ''
    viloyat = Viloyat.objects.all
    if request.method == 'POST':
        viloyatlar = request.POST['viloyat']
        tumanlar = request.POST['tuman']
        if Tuman.objects.filter(tuman=tumanlar):
            habar = 'Bunday tuman mavjud'
        else:
            baza = Tuman.objects.create(viloyat=viloyatlar, tuman=tumanlar)
            baza.save()
        return redirect('/talaba')
    contex = {
        'viloyat' : viloyat,
        'habar' : habar,
    }
    return render(request, 'viloyat/tuman.html', contex)

@csrf_exempt
def mfy(request):
    habar = ''
    viloyat =Viloyat.objects.order_by('viloyat')
    tuman = Tuman.objects.values(viloyat=viloyat)
    if request.method == 'POST':
        viloyatlar = request.POST['viloyat']
        tumanlar = request.POST['tuman']
        mfylar = request.POST['mfy']
        if Mfy.objects.filter(mfy=mfylar):
            habar = 'Bunday MFY mavjud'
        else:
            baza = Mfy.objects.create(viloyat=viloyatlar, tuman=tumanlar, mfy=mfylar)
            baza.save()
        return redirect('/talaba')
    contex = {
        'viloyat':viloyat,
        'tuman':tuman,
        'habar':habar,
    }
    return render(request, 'viloyat/mfy.html', contex)

def sinov(request):
    if request.method == 'POST':
        ism = request.POST['ism']              
        baza = Sinov.objects.create(ism=ism)
        baza.save()

    contex = {
        
    }
    return render(request, 'sinov.html', contex)


from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def update(request, pk):
    data = get_object_or_404(Sinov, pk=pk)

    data.ism = 'alisher'

    data.save()
    


    contex = {
        
    }
    return render(request, 'update.html', contex)

    
    
  
