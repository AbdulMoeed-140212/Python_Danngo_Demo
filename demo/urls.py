from django.contrib import admin
from django.urls import path, include
from drf import urls

urlpatterns = [
    path('', include('drf.urls') ),
    path('admin/', admin.site.urls),
]
