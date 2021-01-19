from django.db import models

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
    answer1 = models.CharField(max_length=50, blank=False, unique=True)
    answer2 = models.CharField(max_length=50, blank=False, unique=True)
    answer3 = models.CharField(max_length=50, blank=False, unique=True)
    answer4 = models.CharField(max_length=50, blank=False, unique=True)
    correctAnswer=models.CharField(max_length=50,blank=False)

    def __str__(self):
        return f"{self.correctAnswer}"
