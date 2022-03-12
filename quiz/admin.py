from django.contrib import admin
from .models import Question, Category, Answer


# Register your models here.
@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'category']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    list_display = ['answer_text', 'is_answer', 'question']
