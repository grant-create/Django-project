from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question



# # def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index.")

# # new Index: 
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,

#     }
#     return render(request, 'polls/index.html', context)



# #https://docs.djangoproject.com/en/3.2/intro/tutorial03/



# def detail(request, question_id):
#     # try: 
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")

#     question = get_object_or_404(Question, pk=question_id)
    

#     #return HttpResponse("You're looking at question %s." %question_id)
#     return render(request, 'polls/detail.html', {'question': question})





# def results(request, question_id):

#     question = get_object_or_404(Question, pk=question_id)
    

#     return render(request, 'polls/results.html', {'question':question})



# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try: 
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form
#         return render(request, 'polls/detail.html',{ 'question': question, 'error_message': "you didnt select a  choice",})

#     else: 
#         selected_choice.votes +=1
#         selected_choice.save()
#         # Always return an HTtpResponseRedirect after successfully dealing with POST data
#         # this prevents data from being posted twice if a user hits the back button




#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))





class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html',{ 'question': question, 'error_message': "you didnt select a  choice",})
    else: 
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HTtpResponseRedirect after successfully dealing with POST data
        # this prevents data from being posted twice if a user hits the back button
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def new(request):
   
    context ={}
    if request.method == "POST":
        print(request.POST['newquestion'])
    
        q = Question(question_text=request.POST['newquestion'], pub_date=timezone.now())
        q.save()
        #print(q)
        q.choice_set.create(choice_text=request.POST['choice1'], votes=0)
        q.choice_set.create(choice_text=request.POST['choice2'], votes=0)
        
    #return render(request, 'poll/index.html')
    #return HttpResponse("You're making a new question")

        
    return render(request, 'polls/new.html', context)
