from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404,render
from django.view import generic

from .models import Question, Choice

# Create your views here.
#def index(request):
#	lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#	context = {'lastest_question_list': lastest_question_list}
#	return render(request, 'polls/index.html', context)
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'lastest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by("-pub_date")[:5]

#def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#question = get_object_or_404(Question, pk=question_id)
	#return render(request, 'polls/detail.html', {'question': question})
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

#def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/results.html', {'question': question})
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
	
# 处理请求
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
