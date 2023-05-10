from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
from .models import Fakultet, Kafedra, Yonalish, Kurs, Guruh
 
@csrf_exempt  
def fakultet(request):
    if request.method == 'POST':
        fakultetlar = request.POST['fakultet']
        if Fakultet.objects.filter(fakultet=fakultetlar):
            habar = 'Bunday fakultet mavjud'
        else:
            baza = Fakultet.objects.create(fakultet=fakultetlar)
            baza.save()
            return redirect('/')
    return render(request, 'dekanat/fakultet/fakultet_yangi.html')


@csrf_exempt  
def yonalish(request):
    if request.method == 'POST':
        yonalishlar = request.POST['yonalish']
        if Yonalish.objects.filter(yonalish=yonalishlar):
            habar = 'Bunday yonalish mavjud'
        else:
            baza = Yonalish.objects.create(yonalish=yonalishlar)
            baza.save()
            return redirect('/')
    return render(request, 'dekanat/yonalish/yonalish_yangi.html')

@csrf_exempt  
def kurs(request):
    if request.method == 'POST':
        kurslar = request.POST['kurs']
        if Kurs.objects.filter(kurs=kurslar):
            habar = 'Bunday kurs mavjud'
        else:
            baza = Kurs.objects.create(kurs=kurslar)
            baza.save()
            return redirect('/')
    return render(request, 'dekanat/kurs/kurs_yangi.html')


@csrf_exempt  
def guruh(request):
    if request.method == 'POST':
        guruhlar = request.POST['guruh']
        if Guruh.objects.filter(guruh=guruhlar):
            habar = 'Bunday guruh mavjud'
        else:
            baza = Guruh.objects.create(guruh=guruhlar)
            baza.save()
            return redirect('/')
    return render(request, 'dekanat/guruh/guruh_yangi.html')

@csrf_exempt
def kafedra(request):
    habar = ''
    if request.method == 'POST':
        fakultetlar = request.POST['fakultet']
        kafedralar = request.POST['kafedra']
        if Kafedra.objects.filter(kafedra=kafedralar):
            habar = 'Bunday kafedra mavjud'
        else:
            baza = Kafedra.objects.create(fakultet=fakultetlar, kafedra=kafedralar)
            baza.save()
        return redirect('/')
    contex = {
        'habar':habar,
    }
    return render(request, 'dekanat/kafedra/kiritish.html')

@csrf_exempt
def fakultetlar(request):
    kafedralar = Kafedra.objects.all   
    fakultetlar = Fakultet.objects.all()
    
    contex = {
        'fakultetlar':fakultetlar,
        'kafedralar':kafedralar,
    }
    return render(request, 'dekanat/fakultet/fakultetlar.html', contex)