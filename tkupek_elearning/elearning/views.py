from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response

from tkupek_elearning.elearning.models import Setting, Question, Option, UserAnswer, User

# import pdb

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


def get_answer(request):
    if request.method == 'GET':

        request_id = request.GET.get('id')
        request_token = request.GET.get('token')
        request_answers = request.GET.get('answers')

        question = Question.objects.get(id=request_id)
        user = User.objects.get(token=request_token)

        try:
            user_answer = UserAnswer.objects.get(questionId=question.id, user=user.id)
        except ObjectDoesNotExist:
            user_answer = None

        if user_answer is None:
            user_answer = UserAnswer()
            user_answer.questionId = question
            user_answer.user = user
            user_answer.answers = request_answers
            user_answer.save()

        options = Option.objects.filter(question=question.id, correct=True)

        options_id = ""
        for option in options:
            options_id += str(option.id) + "_"

        if options_id is not "":
            options_id = options_id[:-1]

        return HttpResponse(options_id)
