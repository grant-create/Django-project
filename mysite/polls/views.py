from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

from .models import Question


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# new Index: 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,

    }
    return render(request, 'polls/index.html', context)



#https://docs.djangoproject.com/en/3.2/intro/tutorial03/



def detail(request, question_id):
    # try: 
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    

    #return HttpResponse("You're looking at question %s." %question_id)
    return render(request, 'polls/detail.html', {'question': question})





def results(request, question_id):
    response = "you're looking at the results of question %s" 
    return HttpResponse(response % question_id)



def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)