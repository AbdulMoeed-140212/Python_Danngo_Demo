from django.db import models
from uuid import uuid4

class UserDemo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable= False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    # TimeStamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
