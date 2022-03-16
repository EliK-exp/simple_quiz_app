from django.contrib import admin
from django.db.models import Count

from .models import Question, Category, Answer


# Register your models here.
@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'category']
    # I should provide a link to relative answers later


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'number_of_category_questions']

    @admin.display(ordering='category_questions_count')
    def number_of_category_questions(self, categoty):
        return categoty.question_set.all().count()

    def get_queryset(self, request):
        # print(super(AdminCategory, self).get_queryset(request).first().question_set.all())
        qs = super().get_queryset(request)
        return qs.annotate(
            category_questions_count=Count('question'))  # I do not know why it is question and not questions-set!


@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    list_display = ['answer_text', 'is_answer', 'question']
