from django import forms
from django.contrib import admin

from app.models import Profile
from app.models import Folder
from app.models import Document
from app.models import History

class FolderForm(forms.ModelForm):

    folder_name = ''

    class Meta:
        model = Folder
        fields = "__all__"

    def clean_name(self):

        self.folder_name = self.cleaned_data['name']

        return self.folder_name

    def clean_parent(self):
        parent_name  = self.cleaned_data['parent']

        if self.folder_name in Folder.objects.filter(
            parent=parent_name
        ).values_list('name', flat=True):
            raise forms.ValidationError(
                'Ya existe la carpeta en la misma ubicación!'
            )
        return parent_name


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    form = FolderForm
    list_display = ('pk', 'name', 'parent', 'is_public')
    list_display_links = ('pk','name')
    search_fields = ('pk', 'name')
    list_filter = ('created_at', 'is_public')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'username', 'email', 'role', 'is_staff', 'is_active')
    list_display_links = ('pk', 'username', 'email',)
    search_fields = ('pk', 'email', 'username')
    list_filter = ('created_at', 'is_active', 'is_staff', 'role')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = ('pk', 'serie', 'name', 'is_public', 'parent', 'file')
    list_display_links = ('pk','serie', 'name')
    search_fields = ('pk', 'serie', 'name' )
    list_filter = ('is_public', 'created_at', 'updated_at')



@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):

    list_display = ('pk', 'document', 'user', 'date')
    list_display_links = ('pk','document')
    search_fields = ('pk', 'document')
    list_filter = ('date', 'document')


