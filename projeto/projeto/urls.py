# views.py
from django.urls import path
from django.contrib import admin
from core.views import *

urlpatterns = [
    path('',index),
    path('',home),
    path('',detalhes_curso),
    path('',disciplina),
    path('',lista_cursos),
    path('',noticias),
    path('admin/',admin.site.urls),
]
