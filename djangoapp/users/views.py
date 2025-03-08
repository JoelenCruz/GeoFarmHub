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
            return redirect("login")  # Após o registro, redireciona para a tela de login
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
    return redirect("login")  # Redireciona para a tela de login após logout




def client_list(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients, "form": form})

def farm_list(request):
    if request.method == "POST":
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_list')
    else:
        form = FarmForm()

    farms = Farm.objects.all()
    return render(request, "farms.html", {"farms": farms, "form": form})

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
