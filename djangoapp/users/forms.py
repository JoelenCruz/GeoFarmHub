import json
from django.contrib.gis.geos import GEOSGeometry
from django import forms
from .models import Client
from .models import Transaction
from .models import Farm
from osgeo import ogr

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from .models import Farm


def parse_kml_file(kml_file):
    ds = DataSource(kml_file)
    layer = ds[0]
    feature = layer[0]
    geom = feature.geom
    return GEOSGeometry(geom.wkb)

# forms.py
from django import forms
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from .models import Farm

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ["name", "owner", "area_hectares", "kml_file"]
        # "location" será preenchido automaticamente via parse do KML

    def clean_kml_file(self):
        """
        1. Garante que o arquivo é um KML válido.
        2. Retorna o arquivo, caso precise armazená-lo.
        (O parse para geometria faremos no 'save()' ou na view.)
        """
        file = self.cleaned_data.get("kml_file")
        if not file:
            return None

        # Testa se o arquivo KML é válido (parse básico)
        try:
            ds = DataSource(file)
            # Se não der erro aqui, significa que é um KML/arquivo GIS reconhecível.
        except Exception:
            raise forms.ValidationError("Arquivo KML inválido ou não pôde ser interpretado.")

        return file




class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['client', 'farm', 'transaction_type', 'price']




