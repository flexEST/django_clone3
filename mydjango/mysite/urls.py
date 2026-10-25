from django.contrib import admin
from django.urls import path
from steam import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("steam/", views.home, name="home"),
]
