from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Edicao, Noticia, Comentario, Usuario

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['titulo', 'descricao']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']

class CadastroForm(UserCreationForm):
    nome = forms.CharField(max_length=50, label="Nome e sobrenome")
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )
        nome = self.cleaned_data['nome']
        usuario = Usuario(nome=nome, user=user)
        if commit:
            usuario.save()
        return usuario