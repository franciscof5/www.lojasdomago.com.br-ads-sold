from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from django.conf.urls.static import static

global GLOBAL_VAR_X
GLOBAL_VAR_X = []    # Global var
# Create your views here.
def index(request):
    global GLOBAL_VAR_X
    path = "/Users/francisco/Downloads/anuncios-controle/usados/"
    #path = static 
    dir_scan(path)

    #dd()
    return HttpResponse(GLOBAL_VAR_X)


def dir_scan(path):
    global GLOBAL_VAR_X
    path_trocar = "/Users/francisco/Downloads/anuncios-controle/"
    #text="dir_scan"
    for i in os.scandir(path):
        if i.is_file() and i.path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            trocado = i.path.replace(path_trocar, "/static/")
            GLOBAL_VAR_X.append('<img src="' + trocado + '" width="200">') 
        elif i.is_dir():
            trocado = i.path.replace(path_trocar + "usados/", "")
            GLOBAL_VAR_X.append('<h3>' + trocado + '</h3>')
            dir_scan(i.path)