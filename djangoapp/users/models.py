from django.contrib.gis.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()  # Ensure PostGIS is enabled
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)  # Add this field if missing
    area_hectares = models.DecimalField(max_digits=10, decimal_places=2)  # Add this if needed

    def __str__(self):
        return self.name

class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10, choices=[("buy", "Buy"), ("sell", "Sell")])
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # ✅ Add this line if missing




    def __str__(self):
        return f"{self.client} - {self.farm} ({self.transaction_type})"
