from .models import *

def menu_links(request):
    links = Project.objects.all()
    return dict(links=links)