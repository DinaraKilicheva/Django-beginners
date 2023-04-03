from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def questions_list(request):
    # questions = Question.objects.all().filter(text__icontains="o")
    # response = ''
    # for index, question in enumerate(questions):
    #     response += f"{index + 1}.{question.text}<br>"
    # return HttpResponse(f"questions list here.<br>{response}")
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'polls/questions.html', context=context)


def question_detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    #
    # except Question.DoesNotExist:
    #     # return HttpResponse("Not found")
    #     raise Http404
    # else:
    # #     return HttpResponse(f"Questions text: {question.text}<br>pub_date:{question.pub_date}")
    # question = get_object_or_404(Question, id=question_id)
    # return HttpResponse(f"Questions text: {question.text}<br>pub_date:{question.pub_date}")
    question = get_object_or_404(Question, id=question_id)
    context={
        "question":question
    }
    return render(request, 'polls/question_detail.html',context=context)
