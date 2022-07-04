from statistics import mode
from django.db import models


# Site Modele


class Site(models.Model):
    IdSite=models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Description = models.TextField()
# Departement Modele


class Departement(models.Model):
    IdDepartement=models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Site = models.ForeignKey('Site', null=True, on_delete=models.CASCADE)
   # Site=models.ForeignKey(Site,on_delete=models.CASCADE)
# Local Modele


class Local(models.Model):
    IdLocal=models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Departement=models.ForeignKey('Departement',on_delete=models.CASCADE)
# Equipement Modele


class Equipement(models.Model):
    class Type(models.TextChoices):
        Routeur = 'R'
        Switch = 'S'
        Fédérateur = 'F'
        MachinePysique = 'MP'
    Name = models.CharField(max_length=100)
    Marque = models.CharField(max_length=100)
    IP_ADD = models.GenericIPAddressField()
    TYPE = models.CharField(choices=Type.choices, max_length=5)
    Local = models.ForeignKey('Local', on_delete=models.CASCADE)


# Contrat  Modele


class Contrat(models.Model):
    class TypeContrat(models.TextChoices):
        ContratMaintenence = 'CM'
        ContratAcquisition = 'CA'
    TypeDeContrat = models.CharField(choices=TypeContrat.choices, max_length=10, default='TypeDeContrat')
    Equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    Fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE)
    DateDebut = models.DateField()
    DateFin=models.DateField()


# Fournisseur Modele
class Fournisseur(models.Model):
    
    Name = models.CharField(max_length=100)
    NameDeEntreprise = models.CharField(max_length=100, default='NomEntreprise')
    Mail = models.EmailField(max_length=254)
    NumeroTéléphone=models.IntegerField()