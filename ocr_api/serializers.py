from ocr.models import *
from rest_framework import serializers




##################################### OCR############################################


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = factures
        fields = ['facture_ID', 'type_facture', 'emetteur', 'client', 'mail_emetteur','date_emission',
                  'date_echeance','conditions', 'total','facture_image'
                  ]


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = produit
        fields = ['id', 'codeProduit', 'nom', 'quantite', 'prix_unitaire', 'somme']


class FactureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyImageModel
        fields = ['id','image']