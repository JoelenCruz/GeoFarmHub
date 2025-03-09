from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ClientForm, FarmForm, TransactionForm
from .models import Client, Farm, Transaction
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry

from django.http import JsonResponse



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
    return redirect("initial")


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


@login_required
def client_list(request):
    clients = Client.objects.all()
    form = ClientForm() 
    return render(request, "client_list.html", {"clients": clients, "form": form})

       
@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()
    form = TransactionForm() 
    return render(request, "transactions.html", {"transactions": transactions, "form": form})






@login_required
def farm_list(request):
    if request.method == "POST":
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            farm = form.save(commit=False)
            kml_file = form.cleaned_data.get('kml_file')

            # If there is a KML file, try to extract geometry
            if kml_file:
                try:
                    ds = DataSource(kml_file)
                    layer = ds[0]
                    feature = layer[0]
                    geom = feature.geom
                    farm.location = GEOSGeometry(geom.wkb)
                except Exception:
                    form.add_error('kml_file', "Could not extract geometry from the KML file.")
                    if _is_ajax(request):
                        return JsonResponse({'error': "Could not extract geometry from the KML file."}, status=400)
                    else:
                        return render(request, "farms_list.html", {
                            "farms": Farm.objects.all(),
                            "form": form
                        })

            # Save the Farm object
            farm.save()

            # If it's an AJAX request, return JSON
            if _is_ajax(request):
                data = {
                    'id': farm.id,
                    'name': farm.name,
                    'owner': farm.owner.name if farm.owner else '',
                    'area_hectares': str(farm.area_hectares),
                }
                return JsonResponse(data, status=201)

            # Otherwise, do a normal redirect
            return redirect('farm_list')
        else:
            # Form invalid
            if _is_ajax(request):
                return JsonResponse({'errors': form.errors}, status=400)
            else:
                return render(request, "farms_list.html", {
                    "farms": Farm.objects.all(),
                    "form": form
                })
    else:
        # GET request
        form = FarmForm()
        farms = Farm.objects.all()
        return render(request, "farms_list.html", {"farms": farms, "form": form})

def _is_ajax(request):
    """
    Checks if the request was made via XMLHttpRequest.
    """
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'
