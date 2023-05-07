from django.urls import path
from . import views
from .views import qr_code,scan, liste_etudiants
urlpatterns = [
 
    path('',views.dashboard,name='Home'),
    path('qr-code/', qr_code, name='qr_code'),
    path('scan/', scan, name='scan'),
    path('etudiants/', liste_etudiants, name='liste_etudiants'),
    path('liste_etudiants/', views.liste_etudiants, name='liste_etudiants'),

]