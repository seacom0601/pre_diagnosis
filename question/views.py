from django.shortcuts import render, get_object_or_404, redirect
from question.models import Question, Option, AnsUser
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home(request):
    if request.GET:
        user = AnsUser()
        user.phone_num = request.GET['phone number']
        if request.GET['phone number'] == "":
            print('error')
        user.save()
        return redirect('question', user.pk)
    return render(request, 'home/home.html')


def question(request, pk):
    user = get_object_or_404(AnsUser, pk=pk)

    num = 1
    if request.POST:
        num = int(request.POST['question_id']) + 1
        user.answer = request.POST['answer'] + str(',')
        user.save()

        if num > 20:
            return redirect('result', pk)

    question_num = get_object_or_404(Question, id=num)

    return render(request, 'question/question.html', {'question': question_num})
