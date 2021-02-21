from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('login/',views.LoginPage,name="Login"),
    path("logout/",views.LogoutPage,name="Logout"),
    path("sign-up/",views.SignUpPage,name="SignUp"),
]
