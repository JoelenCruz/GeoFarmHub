import json
import os
from django.contrib.gis.geos import GEOSGeometry
from django import forms
from .models import Client
from .models import Transaction
from .models import Farm
from osgeo import ogr
from django.contrib.gis.gdal import DataSource




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

import os
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['client', 'farm', 'transaction_type', 'price']

    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get('transaction_type')
        client = cleaned_data.get('client')
        farm = cleaned_data.get('farm')

        if transaction_type == 'sell':
            # Only allow selling if the client is the owner of the farm
            if farm and farm.owner != client:
                raise forms.ValidationError("You can only sell a farm that you own.")

            # Ensure the farm can only be sold once.
            # Option 1: If your Farm model has an "is_sold" field:
            if farm and getattr(farm, 'is_sold', False):
                raise forms.ValidationError("This farm has already been sold.")
        return cleaned_data




