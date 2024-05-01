from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
