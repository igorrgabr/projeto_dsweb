from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Edicao, Noticia
from .forms import EdicaoForm, NoticiaForm, ComentarioForm, CadastroForm

def fazer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('journal:index')
    return render(request, 'registration/login.html')

def fazer_logout(request):
    logout(request)
    return redirect('journal:index')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:login')
    else:
        form = CadastroForm()
    return render(request, 'registration/registration_form.html', {'form': form})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        ultima_edicao = Edicao.objects.latest('data')
        noticias = ultima_edicao.noticia_set.all()
        contexto = {'ultima_edicao': ultima_edicao, 'noticias': noticias}
        return render(request, 'journal/index.html', contexto)

class ListaEdicaoView(View):
    def get(self, request, *args, **kwargs):
        ultima_edicao = Edicao.objects.latest('data')
        lista_edicao = Edicao.objects.exclude(id=ultima_edicao.id)
        contexto = {'lista_edicao': lista_edicao}
        return render(request, 'journal/lista_edicao.html', contexto)

class EdicaoView(View):
    def get(self, request, *args, **kwargs):
        edicao = get_object_or_404(Edicao, pk=kwargs['pk'])
        query = request.GET.get('q', '')
        if query:
            noticias = Noticia.objects.filter(titulo__icontains=query, edicao=edicao)
        else:
            noticias = edicao.noticia_set.all()
        contexto = {'edicao': edicao, 'noticias': noticias, 'query': query}
        return render(request, 'journal/edicao.html', contexto)

class AddEdicaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = EdicaoForm()
        return render(request, 'journal/add_edicao.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = EdicaoForm(request.POST)
        if form.is_valid():
            form.instance.data = timezone.now()
            form.instance.usuario = self.request.user.usuario
            form.save()
            return redirect('journal:index')
        return render(request, 'journal/add_edicao.html', {'form': form})

class NoticiaView(View):
    def get(self, request, *args, **kwargs):
        noticia = get_object_or_404(Noticia, pk=kwargs['pk'])
        comentarios = noticia.comentario_set.all()
        contexto = {'noticia': noticia, 'comentarios': comentarios}
        return render(request, 'journal/noticia.html', contexto)

class AddNoticiaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = NoticiaForm()
        return render(request, 'journal/add_noticia.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = NoticiaForm(request.POST)
        edicao = get_object_or_404(Edicao, pk=kwargs['pk'])
        if form.is_valid():
            form.instance.edicao = edicao
            form.instance.data_pub = timezone.now()
            form.instance.usuario = self.request.user.usuario
            form.save()
            return redirect(reverse('journal:edicao', kwargs={'pk': edicao.pk}))
        return render(request, 'journal/add_noticia.html', {'form': form})

class AddComentarioView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ComentarioForm()
        return render(request, 'journal/add_comentario.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        noticia = get_object_or_404(Noticia, pk=kwargs['pk'])
        if form.is_valid():
            form.instance.noticia = noticia
            form.instance.data_pub = timezone.now()
            form.instance.usuario = self.request.user.usuario
            form.save()
            return redirect(reverse('journal:noticia', kwargs={'pk': noticia.pk}))
        return render(request, 'journal/add_comentario.html', {'form': form})