from . import views
from django.urls import path


urlpatterns = [
    path("menu/", views.menu_view, name="menu"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('clients/', views.client_list, name='client_list'),
    path('farms/', views.farm_list, name='farm_list'),
    path('transactions/', views.transaction_list, name='transaction_list'),
]
