from __future__ import division
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import json

from tkupek_elearning.elearning.models import Setting, Question, Option, UserAnswer, User, UserAnswerOptions


#import pdb


def get_progress(user):
    progress_max = Question.objects.all().count()
    progress_current = UserAnswer.objects.filter(user=user.id).count()
    return int(progress_current / progress_max * 100)


def start(request):

    token = request.GET.get('token')

    try:
        user = User.objects.get(token=token)
    except ObjectDoesNotExist:
        user = None

    try:
        settings = Setting.objects.get(active=1)
    except ObjectDoesNotExist:
        settings = None

    if settings is None:
        return render_to_response('setting_null.html')

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

        progress = get_progress(user)

        return render_to_response('elearning.html', {'settings': settings, 'questions_options': questions_options, 'progress': progress})

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

        correct_options = Option.objects.filter(question=question.id, correct=True)
        correct_option_checklist = []
        for option in correct_options:
            correct_option_checklist.append(option.id)

        options_id = []
        for option in correct_options:
            options_id.append(option.id)

        user_answer = get_user_answer(question, user)

        if user_answer is None:
            correct = False

            user_answer = UserAnswer()
            user_answer.question = question
            user_answer.user = user

            for option in request_answers:
                if option in correct_option_checklist:
                    correct_option_checklist.remove(option)

            if len(correct_option_checklist) is 0:
                correct = True

            user_answer.correct = correct
            user_answer.save()

            for option in request_answers:
                user_answer_options = UserAnswerOptions()
                user_answer_options.user_answer = user_answer
                user_answer_options.option = Option.objects.get(id=option)
                user_answer_options.save()

        progress = get_progress(user)
        show_completed = False
        if progress is 100 and user.completed is False:
            show_completed = True
            user.completed = True
            user.save()

        holder = {'options_id': options_id, 'progress': str(progress), 'show_completed': show_completed}
        holder = json.dumps(holder)

        return HttpResponse(holder)


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

    token = request.GET.get('token')

    try:
        settings = Setting.objects.get(active=1)
    except ObjectDoesNotExist:
        settings = None

    if settings is None:
        return render_to_response('setting_null.html')

    try:
        auth = Setting.objects.get(active=1, statistic_token=token)
    except ObjectDoesNotExist:
        auth = None

    settings = Setting.objects.get(active=1)

    if auth is not None:
        settings = Setting.objects.get(active=1)
        users = User.objects.all()

        for user in users:
            user.questions_answered = UserAnswer.objects.filter(user=user.id).count()

        questions = Question.objects.all()
        for question in questions:
            question.answers = UserAnswer.objects.filter(question=question.id).count()
            question.correct_answers = UserAnswer.objects.filter(question=question.id, correct=True).count()
            if question.answers:
                question.correct_answers_percentage = str(int(question.correct_answers / question.answers * 100))
                question.correct_answers_percentage += str(' %')

        return render_to_response('statistic.html', {'settings': settings, 'users': users, 'questions': questions})

    else:
        return render_to_response('access_denied.html', {'settings': settings})