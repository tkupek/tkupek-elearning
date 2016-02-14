import datetime
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response

from tkupek_elearning.elearning.models import Setting, Question, Option, UserAnswer, User, UserAnswerOptions


import pdb


def start(request):

    token = request.GET.get('token')

    try:
        user = User.objects.get(token=token)
    except ObjectDoesNotExist:
        user = None

    settings = Setting.objects.get(active=1)

    if user is not None:

        log_last_seen(user)

        settings.message_welcome_user = settings.message_welcome_user.replace('{username}', user.name)

        questions_options = {}
        questions = Question.objects.all()
        for question in questions:
            options = Option.objects.filter(question=question.id)

            user_answer = get_user_answer(question, user)

            if user_answer is None:
                question.enable = True
            else:
                question.enable = False

            questions_options[question] = options
            questions_options[question] = options

        return render_to_response('elearning.html', {'settings': settings, 'questions_options': questions_options})

    else:
        return render_to_response('access_denied.html', {'settings': settings})


def get_answer(request):
    if request.method == 'GET':

        request_id = request.GET.get('id')
        request_token = request.GET.get('token')
        request_answers = request.GET.get('answers')
        request_answers = json.loads(request_answers)

        question = Question.objects.get(id=request_id)
        user = User.objects.get(token=request_token)
        log_last_seen(user)

        user_answer = get_user_answer(question, user)

        if user_answer is None:
            user_answer = UserAnswer()
            user_answer.question = question
            user_answer.user = user
            user_answer.save()

            for option in request_answers:
                user_answer_options = UserAnswerOptions()
                user_answer_options.user_answer = user_answer
                user_answer_options.option = Option.objects.get(id=option)
                user_answer_options.save()

        options = Option.objects.filter(question=question.id, correct=True)

        options_id = []
        for option in options:
            options_id.append(option.id)
        options_id = json.dumps(options_id)

        return HttpResponse(options_id)


def get_user_answer(question, user):
    try:
        user_answer = UserAnswer.objects.get(question=question.id, user=user.id)
    except ObjectDoesNotExist:
        user_answer = None

    return user_answer


def log_last_seen(user):
    user.last_seen = datetime.datetime.now()
    user.save()


def statistic(request):

    settings = Setting.objects.get(active=1)
    users = User.objects.all()

    for user in users:
        user.questions_answered = UserAnswer.objects.filter(user=user.id).count()

    questions = Question.objects.all()
    for question in questions:
        question.answers = UserAnswer.objects.filter(question=question.id).count()

    return render_to_response('statistic.html', {'settings': settings, 'users': users, 'questions': questions})
