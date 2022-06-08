import os

from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
import csv


def index(request):
    latest_question_list = Question.objects.all()#.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)

    #print(p)

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        #print(selected_choice)

        with open("output.csv", 'a') as file:
            fwriter = csv.writer(file)
            fwriter.writerow([p.question_text, selected_choice.choice_text])
        #    print(os.path.abspath("result.txt"))
        #file.close()

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {'question': p, 'error_message': "No answer selected."})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})

def downloadFile(request):
    file_name = os.path.basename("output.csv")
    response = FileResponse(open(file_name, 'rb'), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'

    return response
