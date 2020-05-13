from django.db import models

from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords

class Profile(AbstractUser):
    ROLE_CHOICES = (
        (1, 'Empleado'),
        (2, 'Abogado'),
        (3, 'Administrador'),
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        default=3
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']


class Folder(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='nombre'
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='ubicacion'
    )

    is_public = models.BooleanField(
        default=True,
        verbose_name='carpeta publica'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    history = HistoricalRecords()

    def get_name(self):
        if self.parent:
            return f'{self.parent.get_name()}/{self.name}'
        return self.name

    def get_pk(self):
        if self.parent:
            return self.parent.get_pk() + [{'name': self.name, 'pk': self.pk}]
        return [{'name': self.name, 'pk': self.pk}]

    def __str__(self):
        return self.get_name()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Carpeta'
        verbose_name_plural = 'Carpetas'


class Document(models.Model):
    file = models.FileField(
        upload_to='documents'
    )

    name = models.CharField(
        max_length=250,
        verbose_name='nombre'
    )

    parent = models.ForeignKey(
        Folder,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='ubicación'
    )

    serie = models.CharField(
        max_length=250
    )

    is_public = models.BooleanField(
        default=True,
        verbose_name='documento publico'
    )

    comments = models.TextField(
        verbose_name='comentarios',
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def get_pk(self):
        if self.parent:
            return self.parent.get_pk() + [{'name': self.name, 'pk': self.pk}]
        return [{'name': self.name, 'pk': self.pk}]

    class Meta:
        ordering = ['-id']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class History(models.Model):
    user = models.CharField(
        max_length=250,
        verbose_name='usuario'
    )

    document = models.CharField(
        max_length=250,
        verbose_name='documento'
    )

    name_document = models.CharField(
        max_length=250,
        verbose_name='nombre documento'
    )

    serie = models.CharField(
        max_length=250,
        verbose_name='serie'
    )

    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de la acción'
    )

    history = HistoricalRecords()

    def __str__(self):
        return '{} modificó el documento "{}" serie {}'.format(
            self.user,
            self.name_documento,
            self.serie
        )

    class Meta:
        ordering = ['-date']
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'
