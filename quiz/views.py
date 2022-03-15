from django.shortcuts import render, redirect
from .models import Question, Answer, Category
from .forms import CategoryForm, QuestionForm


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


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print('form cleaned data: ')
            print(form.cleaned_data)
            form_data = form.cleaned_data
            the_new_category = Category(name=form_data['category_name'])
            the_new_category.save()
            return redirect('all_categories')
    else:
        form = CategoryForm()
    context = {'current_value': 'type here', 'form': form}
    return render(request, 'quiz/add_category.html', context=context)


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            the_category = Category.objects.filter(name=form_data['category']).get()
            new_question = Question()
            new_question.question_text = form_data['question_text']
            new_question.category = the_category
            new_question.save()
            for key in form_data:
                if str(key).startswith('choice'):
                    if str(form_data[str(key)]).endswith('#answer'):
                        answer_text = str(form_data[str(key)]).removesuffix('#answer')
                        answer = Answer()
                        answer.answer_text = answer_text
                        answer.is_answer = True
                        answer.question = new_question
                    else:
                        answer_text = str(form_data[str(key)])
                        answer = Answer()
                        answer.answer_text = answer_text
                        answer.is_answer = False
                        answer.question = new_question
                    answer.save()

    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'quiz/add_question.html', context=context)
