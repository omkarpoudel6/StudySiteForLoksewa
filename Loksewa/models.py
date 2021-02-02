from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=50,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category}"

class Questions(models.Model):
    question=models.CharField(max_length=255,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question}"

class Answer(models.Model):
    question = models.OneToOneField(Questions,on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=50, blank=False)
    answer2 = models.CharField(max_length=50, blank=False)
    answer3 = models.CharField(max_length=50, blank=False)
    answer4 = models.CharField(max_length=50, blank=False)
    correctAnswer=models.CharField(max_length=50,blank=False)

    def __str__(self):
        return f"{self.correctAnswer}"

class Quiz(models.Model):

    choice=(
        ('pass','pass'),
        ('fail','fail')
    )

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.CharField(max_length=3,blank=False)
    # status=models.CharField(max_length=4,choices=choice,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.score}"
