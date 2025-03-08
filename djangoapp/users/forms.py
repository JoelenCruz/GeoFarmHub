from django import forms
from .models import Client, Farm, Transaction

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['owner', 'name', 'location', 'area_hectares']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['client', 'farm', 'transaction_type', 'price']
