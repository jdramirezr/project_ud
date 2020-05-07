from django.db import models

from django.contrib.auth.models import AbstractUser


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Folder(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='carpeta padre'
    )

    is_private = models.BooleanField(
        default=False,
        verbose_name='es una carpeta privada'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación')

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    def get_name(self):
        if self.parent:
            return f'{self.parent.get_name()} > {self.name}'
        return self.name

    def __str__(self):
        return self.get_name()

    class Meta:
        ordering = ['name']
        verbose_name = 'Carpeta'
        verbose_name_plural = 'Carpetas'


class Document(models.Model):
    file = models.FileField(upload_to='app/documents')
    parent = models.ForeignKey(
        Folder,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='carpeta a la que pertenece el documento'
    )
    name = models.CharField(max_length=250, verbose_name='nombre')
    serie = models.CharField(max_length=250)
    is_private = models.BooleanField(
        default=False,
        verbose_name='es una documento privado'
    )
    comments = models.TextField(verbose_name='nombre')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


class History(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='usuario'
    )
    action = models.CharField(max_length=250, verbose_name='acción')
    document = models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='documento'
    )
    serie = models.CharField(max_length=250)
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de la acción'
    )

    def __str__(self):
        return self.serie

    class Meta:
        ordering = ['-date']
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'