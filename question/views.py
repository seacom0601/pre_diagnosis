from django.shortcuts import render, get_object_or_404, redirect
from home.models import User
from question.models import Question, Sickpart

# Create your views here.

def sick_part(request, id):
    global userid
    user = get_object_or_404(User, pk=id)
    userid = id

    sickparts = Sickpart.objects.all()
    return render(request, 'question template/question2.html', {'sickparts': sickparts})


def sick_part_list(request):
    if request.POST:
        list_item = request.POST.getlist('sick_part')
        sick_part_item = ','.join(list_item)
        user = User.objects.get(pk=userid)
        user.sick_parts = sick_part_item
        user.save()
    return render(request, 'question template/question2.html')


def single_question(request):
    return render(request, 'question template/question.html')
