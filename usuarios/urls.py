from django.urls import path

from usuarios.views import SisgerecuLoginView, SisgerecuLogoutView

urlpatterns = [
    path(r'login/', SisgerecuLoginView.as_view(), name='login'),
    path(r'logout/', SisgerecuLogoutView.as_view(), name="logout")
]