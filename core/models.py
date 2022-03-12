from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class AppUser(AbstractUser):
    # Email field can be overridden here to be unique.
    pass

