from django.db import models

class Usuario(models.Model):
    usu_nome = models.CharField("Nome Usuario",max_length=50)
    usu_senha = models.CharField("Senha Usuario",max_length=6)
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    aluno_nome = models.CharField("Nome Aluno",max_length=50)
    aluno_ra = models.CharField("RA Aluno",max_length=7)
    
    def __str__(self):
        return self.nome

class Professor(models.Model):
    professor_nome = models.CharField("Nome Professor",max_length=50)
    professor_re = models.CharField("Registro Professor",max_length=7)
    
    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField("Nome",max_length=50)
    sigla = models.CharField("Sigla",max_length=5)
    etiqueta = models.SlugField("Etiqueta",max_length=50)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField("Nome",max_length=50)
    etiqueta = models.SlugField("Etiqueta",max_length=50)
    carga_horaria = models.IntegerField("Carga Horária")
    
    def __str__(self):
        return self.nome
