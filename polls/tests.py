import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(txt, d):
    """
    cria uma questão com texto e n° de dias, que pode ser positivo ou negativo, contados a partir do dia corrente
    """
    time = timezone.now() + datetime.timedelta(days=d)
    return Question.objects.create(question_text=txt, pub_date=time)

class QuestionModelTests(TestCase):
    def test_was_pub_with_future_question(self):
        """ método was_published_recently() deve retornar False para questões publicadas no futuro """
        date = timezone.now() + datetime.timedelta(seconds=1)
        future_question = Question(pub_date=date)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_pub_with_old_question(self):
        """ método was_published_recently() deve retornar False para questões publicadas após 48h """
        date = timezone.now() - datetime.timedelta(hours=48, seconds=1)
        old_question = Question(pub_date=date)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_pub_with_recent_question(self):
        """ método was_published_recently() deve retornar True para questões publicadas anterior às 48h """
        date = timezone.now() - datetime.timedelta(hours=47, minutes=59, seconds=59)
        recent_question = Question(pub_date=date)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        caso não existam questões, exibe-se uma mensagem específica
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhuma questão encontrada.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_question(self):
        """
        questões publicadas no passado são exibidas na index
        """
        create_question('Questão no passado.', -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Questão no passado.>'])

    def test_future_question(self):
        """
        questões publicadas no futuro não são exibidas na index
        """
        create_question('Questão no futuro.', 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Nenhuma questão encontrada.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_future_and_past_questions(self):
        """
        apenas questões publicadas no passado são exibidas
        """
        create_question('Questões no passado.', -30)
        create_question('Questão no futuro.', 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Questões no passado.>'])

    def test_two_past_questions(self):
        """
        são exibidas mais de uma questão publicadas no passado
        """
        create_question('Questão no passado 1.', -30)
        create_question('Questão no passado 2.', -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Questão no passado 2.>', '<Question: Questão no passado 1.>'])