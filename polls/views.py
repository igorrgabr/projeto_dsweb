from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.db import models
from django.utils import timezone

from .models import Question, Choice

class IndexView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('qr', '')
        if query:
            question_list = Question.objects.filter(question_text__icontains=query)
        else:
            question_list = Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]
        context = {'question_list': question_list, 'query': query}
        return render(request, 'polls/index.html', context)

class DetailView(View):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        return render(request, 'polls/details.html', {'question': question})

class ResultsView(View):
    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        return render(request, 'polls/results.html', {'question': question})

class VotesView(View):
    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        try:
            choice_id = request.POST['choice']
            selected = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/details.html', {'question':question, 'error':"Selecione uma alternativa válida!",})
        else:
            selected.votes += 1
            selected.save()
            return HttpResponseRedirect(reverse('polls:results', args=(kwargs['pk'],)))



'''
Última vers.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context = 'question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        selected = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {'question':question, 'error':"Selecione uma alternativa válida!",})
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
'''

'''
Penúltima vers.

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

'''

'''
Ver. 2 Index

def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'question_list': question_list}
    return HttpResponse(template.render(context, request))

Ver. 1 Details

def details(request, question_id):
    response = "Você está vendo a questão %s."
    return HttpResponse(response % question_id)

Ver. 2 Details

def details(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Identificador inválido!")
    return render(request, 'polls/details.html', {'question': question})

'''