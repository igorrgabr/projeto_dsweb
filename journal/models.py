from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField("Nome e sobrenome", max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    USERNAME_FIELD = 'user'

    def __str__(self):
        return self.nome

class Edicao(models.Model):
    titulo = models.CharField("Título", max_length=50, blank=False)
    descricao = models.CharField("Descrição", max_length=200, blank=True)
    data = models.DateTimeField("Data de cadastro", blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.data}"

class Noticia(models.Model):
    titulo = models.CharField("Título", max_length=50, blank=False)
    conteudo = models.TextField("Conteúdo", blank=False)
    data_pub = models.DateTimeField("Data de publicação", blank=False)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, null=True, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    conteudo = models.CharField("Conteúdo", max_length=100, blank=False)
    data_pub = models.DateTimeField("Data de publicação", blank=False)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.conteudo} - {self.usuario}"