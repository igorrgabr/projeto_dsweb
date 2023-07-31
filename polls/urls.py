from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/votes/', views.VotesView.as_view(), name='votes'),
]



'''
urlpatterns = [
    path('', views.index, name="index"),
    path('polls/<int:question_id>/', views.details, name="detail"),
    path('polls/<int:question_id>/results/', views.results, name="results"),
    path('polls/<int:question_id>/votes/', views.votes, name="votes"),
]
'''