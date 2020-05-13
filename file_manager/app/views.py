from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.models import Folder, Document

class FolderListParent(ListView):
    template_name = 'folder_list.html'
    queryset = Folder.objects.exclude(parent__isnull=False)
    context_object_name = 'folders'
    paginate_by = 10

class FolderList(ListView):
    template_name = 'folder_list.html'

    def get(self, request, *args, **kwargs):
        folder = Folder.objects.filter(pk=kwargs['pk']).first()
        msg = ''

        if folder:
            folders = Folder.objects.filter(parent=folder)
            documents = Document.objects.filter(parent=folder)
            if not folders and not documents:
                msg = 'No hay documentos'
            return render(
                request,
                self.template_name,
                {
                    'folders':folders,
                    'parents': folder.get_pk(),
                    'documents': documents,
                    'msg': msg
                }
            )
        return render(
            request,
            self.template_name,
            {'msg': 'No existe la carpeta'}
        )
