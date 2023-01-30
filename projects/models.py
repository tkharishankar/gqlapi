import uuid
from pyexpat import model

from django.db import models

# Create your models here.

from django.db import models
import uuid

from users.models import Profile


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
