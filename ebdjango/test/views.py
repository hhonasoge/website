from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question, OpenQuestion, OpenQuestionForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'test/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'test/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "/test/detail.html", {
                'question': question,
                'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('test:results', args=(question.id,)))

def questions(request):
    question = OpenQuestion
    question_form = OpenQuestionForm(instance=question)
    if request.method=='POST':
        question_form = OpenQuestionForm(request.POST)
        question_form.save()
        print "SAVING QUESTION TO DATABASE: Name= " + request.POST.get('name') + " Email= "+ request.POST.get('email') + " Content= "+ request.POST.get('content')
        return HttpResponseRedirect('test/index.html')
    return render(request, 'test/questions.html', {
        'form': question_form,
    })
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'test/results.html', {'question': question})

def about(request):
    return render(request, 'test/about.html')
