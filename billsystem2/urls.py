from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("pdf/", views.generatepdf, name="pdf"),
    path('signup/', views.SignUp, name="sigup"),
    path('login/', views.loginup, name="login"),
    path('logout/', views.logoutpage, name="logout")

]