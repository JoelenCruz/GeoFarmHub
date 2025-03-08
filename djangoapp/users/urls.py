from . import views
from django.urls import path
from django.http import HttpResponse

# Funções temporárias para evitar erro de rota
def placeholder_view(request):
    return HttpResponse("<h1>Em construção...</h1>")


urlpatterns = [
    path("menu/", views.menu_view, name="menu"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("clients/", placeholder_view, name="client_list"),
    path("farms/", placeholder_view, name="farm_list"),
    path("transactions/", placeholder_view, name="transaction_list"),
]
