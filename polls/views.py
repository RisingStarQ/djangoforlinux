import imp
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.http import Http404
from django.urls import reverse

from .models import Choice, Question

# Create your views here.
def index(request):
	# return HttpResponse("这里是polls app的一个投票系统")
	#question 数据按照pub_date 倒叙排列 返回
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ','.join([q.question_text for q in latest_question_list])
	context = {'latest_question_list': latest_question_list}
	# return HttpResponse(output)
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist!!!")
	# return HttpResponse("You're looking at question %s." % question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	# return HttpResponse("You're looking at the results of question %s." % question_id)
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	# print('输出request' + str(request))
	# return HttpResponse("You're voting on question %s." % question_id)
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))