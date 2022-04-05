from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

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
	return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)