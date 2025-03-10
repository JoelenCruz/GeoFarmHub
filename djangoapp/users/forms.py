import json
from django import forms
from django.contrib.gis.geos import GEOSGeometry
from .models import Client
from .models import Transaction
from .models import Farm
from osgeo import ogr
from django.contrib.gis.gdal import DataSource
import os





class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ["name", "owner", "area_hectares", "kml_file"]
    def clean_kml_file(self):
        kml_file = self.cleaned_data.get("kml_file")
        if kml_file:
            ext = os.path.splitext(kml_file.name)[1].lower()  # e.g. ".kml"
            if ext != ".kml":
                raise forms.ValidationError("Please upload a file with a .kml extension.")
        return kml_file




class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['client', 'farm', 'transaction_type', 'price']