from django.shortcuts import render_to_response

from tkupek_elearning.elearning.models import Setting, Question

#import pdb; pdb.set_trace()

def home(request):

    questions = Question.objects.all()
    settings = Setting.objects.filter(active=1)
    if(settings) :
        settings = settings[0]

    return render_to_response('index.html', {'settings': settings, 'questions': questions})