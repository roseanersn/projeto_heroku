# views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return render(request,"index.html")
def home(request):
        return render(request,"home.html")
def detalhes_curso(request):
        return render(request,"detalhes_curso.html")
def disciplina(request):
        return render(request,"disciplina.html")
def lista_cursos(request):
        return render(request,"lista_cursos.html")
def noticias(request):
        return render(request,"noticias.html")
