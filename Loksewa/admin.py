from django.contrib import admin
from .models import Category,Questions,Answer,Quiz

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Questions)
# admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Category)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     readonly_fields = ['category',]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ['question','answer1','answer2','answer3','answer4','correctAnswer',]

class AnswerInline(admin.StackedInline):
    model=Answer
    # extra=1

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    inlines=[
        AnswerInline,
    ]
