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
        client = data.get('client')

        if transaction_type == "sell":
            # Ensure that the client making the sale is the owner of the farm.
            if farm.owner != client:
                raise serializers.ValidationError("You can only sell a farm that you own.")

            # Ensure that the farm has not already been sold.
            if farm.is_sold:
                raise serializers.ValidationError("This farm has already been sold.")
        return data

    def create(self, validated_data):
        transaction = super().create(validated_data)
        # After a successful sale transaction, mark the farm as sold.
        if transaction.transaction_type == "sell" and not transaction.farm.is_sold:
            farm = transaction.farm
            farm.is_sold = True
            farm.save()
        return transaction
