from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [
    path("register/", views.registerPage, name="registerPage"),
    path("login/", views.loginUser, name="loginUser"),
    path("logout/", views.logoutUser, name="logoutUser")
    
]