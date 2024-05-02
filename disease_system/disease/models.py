from django.db import models
from django.contrib.auth.models import User


class WorkPlace(models.Model):
    place = models.CharField(
        max_length=300, unique=True, null=False, blank=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Work Place'
        verbose_name_plural = 'Work Places'

    def __str__(self) -> str:
        return self.place


class Qualification(models.Model):
    qualification = models.CharField(
        max_length=200, unique=True, null=False, blank=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

    def __str__(self) -> str:
        return self.qualification


class Doctor(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to='doctors/')
    speciality = models.ForeignKey(
        Qualification,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='doctor_speciality',
    )
    institution = models.ForeignKey(
        WorkPlace,
        on_delete=models.CASCADE,
        related_name='doctor_institution',
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='notes_user',
    )
    complaint = models.CharField(max_length=3000)
    diagnosis = models.CharField(max_length=2000)
    treatment = models.CharField(max_length=5000)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='notes_doctor',
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self) -> str:
        return (
            f'{self.user.first_name} {self.user.last_name}: {self.diagnosis}'
        )


class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False
    )
    pill = models.CharField(max_length=300)
    date_discharge = models.DateField(editable=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}: {self.pill}'
