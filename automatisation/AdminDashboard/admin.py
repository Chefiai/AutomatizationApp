from django.contrib import admin

from .import models
# Register your models here.

admin.site.register(models.Site)
admin.site.register(models.Departement)
admin.site.register(models.Local)
admin.site.register(models.Equipement)
admin.site.register(models.Contrat)
admin.site.register(models.Fournisseur)
