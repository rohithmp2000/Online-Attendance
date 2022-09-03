from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserRole(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)