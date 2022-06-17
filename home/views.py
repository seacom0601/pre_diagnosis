from django.shortcuts import render
from home.models import User, Patient
from question.models import Question, Sickpart
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    question = Question.objects.all()
    sickpart = Sickpart.objects.all()
    return render(request, 'home template/home.html', {'question':question, 'sickpart':sickpart})


def user_check(request):
    try:
        user = User()
        user.patient_code = Patient.objects.get(patient_code=request.POST['patient_code_'])
    except (KeyError, Patient.DoesNotExist):
        return render(request,'home template/home.html')
    else:
        user.save()
        return HttpResponseRedirect(reverse('question:sick_part', args=[user.pk]))
