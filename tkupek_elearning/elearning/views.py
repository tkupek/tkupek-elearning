from django.shortcuts import render_to_response

from tkupek_elearning.elearning.models import Setting, Question, Option

#import pdb

def home(request):

    settings = Setting.objects.filter(active=1)
    if settings:
        settings = settings[0]

    questions_options = {}
    questions = Question.objects.all()
    for question in questions:
        options = Option.objects.filter(question=question.id)
        questions_options[question] = options

    return render_to_response('index.html', {'settings': settings, 'questions_options': questions_options})
