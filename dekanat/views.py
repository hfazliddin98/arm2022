from django.shortcuts import render,redirect
from .models import Fakultet, Kafedra, Yonalish, Kurs, Guruh
  
def fakultet(request):
    if request.method == 'POST':
        fakultetlar = request.POST['fakultet']
        baza = Fakultet.objects.create(fakultet=fakultetlar)
        baza.save()
        return redirect('/')
    return render(request, 'dekanat/fakultet/kiritish.html')

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

def fakultetlar(request):
    kafedralar = Kafedra.objects.all   
    fakultetlar = Fakultet.objects.all()
    
    contex = {
        'fakultetlar':fakultetlar,
        'kafedralar':kafedralar,
    }
    return render(request, 'dekanat/fakultet/fakultetlar.html', contex)