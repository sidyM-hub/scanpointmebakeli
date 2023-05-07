from django.db import models

# Create your models here.

from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    date_scan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom