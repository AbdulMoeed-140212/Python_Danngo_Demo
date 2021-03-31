from typing import List
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets, mixins, pagination
from .serializers import UserSerializer, UserDemo
from drf_api_logger.models import APILogsModel

# Create your views here.
class HomePage(TemplateView):
    template_name="drf/index.html"

class LogsPage(ListView):
    template_name="drf/logs.html"
    queryset=APILogsModel.objects.all()
    context_object_name = "logs"
    paginate_by = 10

class UserViewset(mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    authentication_classes = [] # To disable csrf protection
    queryset = UserDemo.objects.all().order_by('-updated_at')
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    