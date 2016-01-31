from django.shortcuts import render_to_response

from tkupek_elearning.elearning.models import question

def home(request):

    questions = question.objects.all()

    return render_to_response('index.html', {'questions': questions})