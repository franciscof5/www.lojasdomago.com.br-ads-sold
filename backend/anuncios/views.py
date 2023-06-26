from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from django.conf.urls.static import static
from PIL import Image


global GLOBAL_VAR_X
GLOBAL_VAR_X = []    # Global var
# Create your views here.
def index(request):
    global GLOBAL_VAR_X
    path = "/code/anuncios-controle/usados/"
    #path = static 
    dir_scan(path)

    #dd()
    return HttpResponse(GLOBAL_VAR_X)


def dir_scan(path):
    global GLOBAL_VAR_X
    path_trocar = "/code/anuncios-controle/"
    #text="dir_scan"
    for i in os.scandir(path):
        if i.is_file() and i.path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            trocado = i.path
            trocado = i.path.replace(path_trocar, "/static/")

            foo = Image.open(trocado)  # My image is a 200x374 jpeg that is 102kb large
            
            #foo.size  # (200, 374)
            
            foo = foo.resize((300,300),Image.ANTIALIAS)
            
            trocadonew = trocado[0:-4] + "_lowquality" + trocado[-4:]

            foo.save(trocadonew, optimize=True, quality=75)  # The saved downsized image size is 24.8kb
            GLOBAL_VAR_X.append('<p>' + trocadonew + '</p>')
            #GLOBAL_VAR_X.append('<img src="' + trocadonew + '" width="200">') 
        elif i.is_dir():
            trocado = i.path.replace(path_trocar + "usados/", "")
            GLOBAL_VAR_X.append('<h3>' + trocado + '</h3>')
            dir_scan(i.path)