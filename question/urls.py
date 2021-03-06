"""project_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [

    path('sick_part/<int:id>/', views.sick_part, name='sick_part'),
    path('sick_part/question_list/', views.question_list, name='question_list'),
    path('<int:question_id>/', views.single_question, name='single_question'),
    path('single_answer/', views.single_answer, name='single_answer'),
    path('next_question/', views.next_question, name='next_question')
]
