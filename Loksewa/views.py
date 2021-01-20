from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Questions,Answer

import random

# Create your views here.
def test(request):
    if request.method=="POST":
        correct=0
        questions=Questions.objects.all()
        print(request.POST)
        for x in request.POST:
            print("request",x)
            for y in questions:
                if x==str(y.id):
                    if y.answer.correctAnswer == request.POST[x]:
                        correct=correct+1
        context={
            'correctAnswer':correct,
            'examcompleted':True
        }
        return render(request,'test.html',context)

    questions = Questions.objects.all().order_by("-created_at")
    examquestions=get_random_questions(questions)
    context={
        'questions':examquestions
    }
    return render(request,'test.html',context)

def questions(request):
    questions = Questions.objects.all().order_by("-created_at")
    questions = get_random_questions(questions)
    context = {
        'questions': questions
    }
    return render(request,'questions.html',context)


def get_random_questions(q):
    questions=[]
    while len(questions)<5:
        question=random.choice(q)
        if question not in questions:
            questions.append(question)
    return questions