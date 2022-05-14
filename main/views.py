from django.views.generic import ListView, CreateView
from .models import Question, Response
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Question
    template_name = 'main/home.html'
    context_object_name = 'all_questions'


class AddQuestionView(SuccessMessageMixin, CreateView):
    model = Question
    fields = '__all__'
    template_name = 'main/add_question.html'
    success_url = reverse_lazy('home')
    success_message = 'Your question successfully added! Soon you will get answers.'


class RespondQuestionView(SuccessMessageMixin, CreateView):
    model = Response
    fields = '__all__'
    template_name = 'main/answer_question.html'
    success_url = reverse_lazy('home')
    success_message = 'You have successfully responded to the question'
