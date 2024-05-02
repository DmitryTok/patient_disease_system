from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
