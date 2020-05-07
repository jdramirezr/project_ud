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
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

class Folder(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='carpeta padre'
    )

    is_public = models.BooleanField(
        default=True,
        verbose_name='carpeta publica'
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
        ordering = ['-id']
        verbose_name = 'Carpeta'
        verbose_name_plural = 'Carpetas'


class Document(models.Model):
    file = models.FileField(upload_to='app/documents')
    parent = models.ForeignKey(
        Folder,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='ruta del documento'
    )
    name = models.CharField(max_length=250, verbose_name='nombre')
    serie = models.CharField(max_length=250)
    is_public = models.BooleanField(
        default=True,
        verbose_name='documento publico'
    )
    comments = models.TextField(verbose_name='comentarios', blank=True)
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
        ordering = ['-id']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class History(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de la acción'
    )

    def __str__(self):
        return f'{self.document.name} - {self.document.serie}'

    class Meta:
        ordering = ['-date']
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'