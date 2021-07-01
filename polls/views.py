from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int):
    return HttpResponse(f"You are looking at the results of question {question_id}.")


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You are voting on question {question_id}.")
