from django import forms
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from app.models import Document
from app.models import Folder
from app.models import History
from app.models import Profile
from app.utils import my_sons_by_pk

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
        ).exclude(pk=self.instance.pk).values_list('name', flat=True):

            raise forms.ValidationError(
                'Ya existe la carpeta!'
            )

        return parent_name


class DocumentForm(forms.ModelForm):

    document_name = ''

    class Meta:
        model = Document
        fields = "__all__"

    def clean_name(self):
        self.document_name = self.cleaned_data['name']

        return self.document_name

    def clean_serie(self):
        serie = self.cleaned_data['serie']

        if Document.objects.filter(serie=serie).exclude(pk=self.instance.pk):
            raise forms.ValidationError(
                'Ya existe el numero de serie!'
            )

        return serie

    def clean_parent(self):
        parent_name  = self.cleaned_data['parent']

        if self.document_name in Document.objects.filter(
            parent=parent_name
        ).exclude(pk=self.instance.pk).values_list('name', flat=True):

            raise forms.ValidationError(
                'Ya existe el documento!'
            )
        return parent_name


@admin.register(Folder)
class FolderAdmin(SimpleHistoryAdmin):
    form = FolderForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        pk_folder = request.resolver_match.kwargs.get('object_id')

        if pk_folder:
            if db_field.name == "parent":
                kwargs["queryset"] = Folder.objects.exclude(
                    pk__in=my_sons_by_pk(
                        element=Folder.objects.get(pk=pk_folder),
                        pk_folder=pk_folder
                    )
                )

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('id', 'name', 'parent', 'is_public')
    list_display_links = ('id','name')
    search_fields = ('id', 'name')
    list_filter = ('created_at', 'is_public')


@admin.register(Profile)
class ProfileAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_staff', 'is_active')
    list_display_links = ('id', 'username', 'email',)
    search_fields = ('id', 'email', 'username')
    list_filter = ('created_at', 'is_active', 'is_staff', 'role')


@admin.register(Document)
class DocumentAdmin(SimpleHistoryAdmin):
    form = DocumentForm
    list_display = ('id', 'serie', 'name', 'is_public', 'parent', 'file')
    list_display_links = ('id','serie', 'name')
    search_fields = ('id', 'serie', 'name' )
    list_filter = ('is_public', 'created_at', 'updated_at')


@admin.register(History)
class HistoryAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'serie', 'name_document','document', 'user', 'date')
    list_display_links = ('id','serie')
    search_fields = ('id', 'serie', 'name_document')
    list_filter = ('date', 'user', 'name_document')


