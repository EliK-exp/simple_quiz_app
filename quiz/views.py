from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request, 'quiz/home.html', context=context)


def all_categories(request):
    context = {}
    return render(request, 'quiz/all_categories.html', context=context)


def all_questions(request):
    context = {}
    return render(request, 'quiz/all_questions.html', context=context)
