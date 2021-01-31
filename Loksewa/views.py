from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage

from .models import Questions,Category,Quiz


import random


# Create your views here.
@login_required(login_url='/login')
def test(request):
    if request.method=="POST":
        correct=0
        questions=Questions.objects.all()
        for x in request.POST:
            for y in questions:
                if x==str(y.id):
                    if y.answer.correctAnswer == request.POST[x]:
                        correct=correct+1
        quiz=Quiz(user=request.user,score=correct)
        quiz.save()
        category=Category.objects.all()
        context={
            'correctAnswer':correct,
            'examcompleted':True,
            'category':category
        }
        return render(request,'test.html',context)

    questions = Questions.objects.all().order_by("-created_at")
    category=Category.objects.all()
    examquestions=get_random_questions(questions,10)
    context={
        'questions':examquestions,
        'category':category
    }
    return render(request,'test.html',context)

@login_required(login_url='/login')
def questions(request):
    category=Category.objects.all()
    questions = Questions.objects.all().order_by("-created_at")
    questions = get_random_questions(questions,10)
    p=Paginator(questions,5)
    page_num=request.GET.get('page',1)
    try:
        paginatedquestions=p.page(page_num)
    except EmptyPage:
        paginatedquestions=p.page(1)
    context = {
        'questions': paginatedquestions,
        'category':category
    }
    return render(request,'questions.html',context)

@login_required(login_url='/login')
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