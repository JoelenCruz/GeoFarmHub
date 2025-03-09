from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Client, Farm, Transaction
from .forms import ClientForm, FarmForm, TransactionForm


@login_required
def menu_view(request):
    return render(request, "menu.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "initial")  


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("menu")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def client_list(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Ensure this matches the name in urls.py
    else:
        form = ClientForm()

    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients, "form": form})  # Ensure correct template path


       

@login_required
def transaction_list(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all()
    return render(request, "transactions.html", {"transactions": transactions, "form": form})



# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from .models import Farm
from .forms import FarmForm

@login_required
def farm_list(request):
    if request.method == "POST":
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            farm = form.save(commit=False)
            # Agora pegamos o arquivo validado
            kml_file = form.cleaned_data.get('kml_file')

            if kml_file:
                # Tenta abrir e extrair a geometria
                try:
                    ds = DataSource(kml_file)
                    layer = ds[0]
                    feature = layer[0]
                    geom = feature.geom  # OGR geometry
                    farm.location = GEOSGeometry(geom.wkb)  # Armazena a geometria no campo location
                except Exception:
                    # Se houver falha no parse, você pode decidir o que fazer:
                    # - Remover farm.kml_file?
                    # - Retornar form com erro?
                    form.add_error('kml_file', "Não foi possível extrair geometria do KML.")
                    return render(request, "farms_list.html", {
                        "farms": Farm.objects.all(),
                        "form": form
                    })

            farm.save()
            return redirect('farm_list')
    else:
        form = FarmForm()

    farms = Farm.objects.all()
    return render(request, "farms_list.html", {"farms": farms, "form": form})

