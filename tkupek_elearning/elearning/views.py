from django.http import HttpResponse
from django.shortcuts import render_to_response

from tkupek_elearning.elearning.models import Setting, Question, Option, UserAnswer, User

import pdb

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


def getAnswer(request):

    # if request.method == 'GET':
    #     pdb.set_trace()
    #     request_questionId = request.GET.get('id')
    #     request_answers = request.GET.get('answers')
    #     request_userToken = request.GET.get('user')
    #
    #     question = Question.objects.filter(questionId=request_questionId)
    #     user = User.objects.filter(token=request_userToken)
    #
    #     userAnswer = UserAnswer.objects.filter(questionId=question.id, user=user.token)
    #     if not userAnswer:
    #         userAnswer = UserAnswer()
    #         userAnswer.questionId = question
    #         userAnswer.user = user
    #         userAnswer.answers = ""
    #         userAnswer.save()
    #     else:
    #         return HttpResponse('error:alreadyAnswered');
    #
    #     options = Option.objects.filter(question=question.id)
    #
    #     return HttpResponse(options)
