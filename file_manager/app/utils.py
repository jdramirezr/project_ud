from .models import Folder


def my_sons_by_pk(element, pk_folder):
    my_sons = [pk_folder]

    def by_pk(element):
        results = Folder.objects.filter(parent=element)
        if results:
            for folder in results:
                my_sons.append(folder.pk)
                by_pk(element=folder)
        return my_sons

    return by_pk(element=element)