from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'pointme/dashboard.html')


import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from .models import Etudiant

def qr_code(request):
    # Générer le QR code avec le lien vers la vue "scan"
    url = request.build_absolute_uri('/scan/')
    img = qrcode.make(url)

    # Afficher l'image du QR code
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

from datetime import datetime
from pyzbar import pyzbar
from django.shortcuts import render, redirect
from .models import Etudiant

def scan(request):
    # Récupérer les données du QR code scanné
    img_data = request.FILES.get('image')
    img = pyzbar.decode(img_data)

    # Ajouter les informations de l'étudiant à la base de données
    if img:
        nom = img[0].data.decode('utf-8')
        telephone = request.POST.get('telephone')
        etudiant = Etudiant.objects.create(nom=nom, telephone=telephone)
        etudiant.save()

    return redirect('qr_code')

from django.shortcuts import render
from .models import Etudiant

def liste_etudiants(request):
    # Récupérer la liste des étudiants scannés
    etudiants = Etudiant.objects.all()

    # Afficher la liste des étudiants scannés dans un template
    return render(request, 'etudiants.html', {'etudiants': etudiants})

