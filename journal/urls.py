from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('edicao/', views.ListaEdicaoView.as_view(), name="lista_edicao"),
    path('edicao/<int:pk>/', views.EdicaoView.as_view(), name="edicao"),
    path('edicao/cadastro/', views.AddEdicaoView.as_view(), name="add_edicao"),
    path('noticia/<int:pk>/', views.NoticiaView.as_view(), name="noticia"),
    path('noticia/cadastro/<int:pk>/', views.AddNoticiaView.as_view(), name="add_noticia"),
    path('comentario/<int:pk>', views.AddComentarioView.as_view(), name="add_comentario"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.fazer_login, name='login'),
    path('accounts/registration/', views.cadastro, name='registration'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]