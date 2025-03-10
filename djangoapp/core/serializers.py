# api/serializers.py
from rest_framework import serializers
from users.models import Client, Farm, Transaction

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        farm = data.get('farm')
        transaction_type = data.get('transaction_type')

        # Exemplo de regra: se for "sell" e a fazenda já estiver vendida, dá erro.
        # (Isso depende de como você define "is_sold" no modelo.)
        if transaction_type == "sell" and farm.is_sold:
            raise serializers.ValidationError("Esta fazenda já foi vendida.")

        return data

    def create(self, validated_data):
        transaction = super().create(validated_data)
        if transaction.transaction_type == "sell" and not transaction.farm.is_sold:
            farm = transaction.farm
            farm.is_sold = True
            farm.save()
        return transaction
