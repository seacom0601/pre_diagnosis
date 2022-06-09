from django.shortcuts import render, get_object_or_404, redirect
from home.models import User
from question.models import Question, Sickpart, Option

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def sick_part(request, id):
    global userid
    user = get_object_or_404(User, pk=id)
    userid = id

    sickparts = Sickpart.objects.all()
    return render(request, 'question template/sickparts.html', {'sickparts': sickparts})


def question_list(request):
    if request.POST:
        sick_part_list = request.POST.getlist('sick_part')
        sick_part_str = ','.join(sick_part_list)
        user = User.objects.get(pk=userid)
        user.sick_parts = sick_part_str
        user.save()

    global questions
    questions = []
    for sickpart in sick_part_list:
        question = Question.objects.filter(sick_part=sickpart)
        for q in question:
            questions.append(q)

    # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return HttpResponseRedirect(reverse('question:next_question'))


def single_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question template/question.html', {'question': question})


def single_answer(request, question_id):
    if type(request.POST) == str:
        user = User.objects.get(pk=userid)
        user.answer = user.answer + ',' + request.POST['option']

    return HttpResponseRedirect(reverse('question:next_question'))

idx = 0
def next_question(request):
    global idx
    if idx < len(questions):
        q = questions[idx]

        idx += 1
        return HttpResponseRedirect(reverse('question:single_question', args=[q.pk]))
    else:
        exit()
