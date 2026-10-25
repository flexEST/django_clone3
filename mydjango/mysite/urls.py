from django.contrib import admin
from django.urls import path
from bina import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("steam/", views.home, name="home"),
]
