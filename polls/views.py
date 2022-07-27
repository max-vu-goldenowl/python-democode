# from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question
# Create your views here.

# def index(request):
#   questions = Question.objects.order_by('-published_date')[:5]
#   return render(request, 'polls/index.html', { 'questions': questions })

# def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/detail.html', { 'question': question })

# def results(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', { 'question': question })

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'questions'

  def get_queryset(self):
    # Returns the last five publised questions
    return Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detals.html'

  def get_queryset(self):
    """
    Excludes any questions that aren't published yet.
    """
    return Question.objects.filter(published_date__lte=timezone.now())

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except(KeyError, Choice.DoesNotExist):
    return render(request, 'polls/details.html', {'question': question, 'error_message': "You didn't select a choice."})
  else:
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def login(request):
  return render(request, 'polls/login.html')
