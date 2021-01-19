from django.http import HttpResponse
from django.shortcuts import render
from .models import Questions,Answer

# Create your views here.
def index(request):
    questions=Questions.objects.all().order_by("-created_at")
    context={
        'questions':questions
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')