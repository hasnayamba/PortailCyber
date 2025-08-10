from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('citoyen', 'Citoyen'),
        ('autorite', 'Autorité'),
        ('expert', 'Expert'),
        ('admin', 'Administrateur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citoyen')

    def __str__(self):
        return f"{self.username} ({self.role})"
