from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Questions,Category

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
        category=Category.objects.all()
        context={
            'correctAnswer':correct,
            'examcompleted':True,
            'category':category
        }
        return render(request,'test.html',context)

    questions = Questions.objects.all().order_by("-created_at")
    category=Category.objects.all()
    examquestions=get_random_questions(questions,5)
    context={
        'questions':examquestions,
        'category':category
    }
    return render(request,'test.html',context)

def questions(request):
    category=Category.objects.all()
    questions = Questions.objects.all().order_by("-created_at")
    questions = get_random_questions(questions,10)
    context = {
        'questions': questions,
        'category':category
    }
    return render(request,'questions.html',context)

def category(request,id):
    category=Category.objects.all()
    questions=Questions.objects.filter(category_id=id)
    categoryaccessed = questions[0].category
    context={
        'category':category,
        'categoryaccessed':categoryaccessed,
        'questions':questions
    }
    return render(request,'categories.html',context)


def get_random_questions(q,n):
    questions=[]
    while len(questions)<n:
        question=random.choice(q)
        if question not in questions:
            questions.append(question)
    return questions