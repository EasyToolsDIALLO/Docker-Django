from django.db import models

# Create your models here.


class factures(models.Model):
    facture_ID = models.CharField(max_length=50, primary_key=True)
    type_facture = models.CharField(max_length=50)
    emetteur = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    mail_emetteur = models.CharField(max_length=50)
    date_emission = models.CharField(max_length=50)
    date_echeance = models.CharField(max_length=50)
    conditions = models.CharField(max_length=50)
    total = models.FloatField()
    facture_image = models.ImageField(
        null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.facture_ID


class MyImageModel(models.Model):
    image = models.ImageField(upload_to='images/')


class produit(models.Model):
    codeProduit = models.ForeignKey('factures', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    quantite = models.IntegerField()
    prix_unitaire = models.FloatField()
    somme = models.FloatField()

    def __str__(self):
        return self.nom
