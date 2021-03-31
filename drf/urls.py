from django.conf.urls import include
from django.urls import path, include
from drf import views
from rest_framework.routers import SimpleRouter


simpleRouter = SimpleRouter()
simpleRouter.register("api", views.UserViewset, basename="api")

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('', include(simpleRouter.urls)),
    path('logs',views.LogsPage.as_view(), name='logs'),
]