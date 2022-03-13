from django.shortcuts import render, redirect
from .models import Question, Answer, Category


# Create your views here.
def home(request):
    context = {}
    return render(request, 'quiz/home.html', context=context)


def all_categories(request):
    categories = Category.objects.prefetch_related('question_set').all()
    context = {'all_categories': categories}
    return render(request, 'quiz/all_categories.html', context=context)


def all_questions(request):
    questions = Question.objects.select_related('category').prefetch_related('answer_set').all()
    context = {'all_questions': questions}
    return render(request, 'quiz/all_questions.html', context=context)


def category_detail(request, category_id):
    the_category = Category.objects.filter(id=category_id).get()
    category_questions = Question.objects.select_related('category').prefetch_related('answer_set').filter(
        category=the_category)
    # context = {'the_category': the_category}
    context = {'the_category': the_category, 'category_questions': category_questions}
    return render(request, 'quiz/category_detail.html', context=context)


def delete_category(request, category_id):
    the_category = Category.objects.filter(id=category_id).get()
    the_category.delete()
    return redirect('all_categories')
