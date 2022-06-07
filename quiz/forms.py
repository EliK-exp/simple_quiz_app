from django import forms
from .models import Category
from django.core.exceptions import ValidationError


class CategoryForm(forms.Form):
    category_name = forms.CharField(label='Category Name ', max_length=100, initial='')


class QuestionForm(forms.Form):
    categories = Category.objects.all()
    ANSWER_CANDIDATES = [(1, '1'), (2, '2'), (3, '3'), (4, '4')]

    question_text = forms.CharField(label='Question', max_length=255)
    choice_one = forms.CharField(label='Choice 1', max_length=255)
    choice_two = forms.CharField(label='Choice 2', max_length=255)
    choice_three = forms.CharField(label='Choice 3', max_length=255)
    choice_four = forms.CharField(label='Choice 4', max_length=255)
    category = forms.ModelChoiceField(label='Select the Category :', queryset=categories)

    # Check if there is only one answer, not less not more! Also checks if a field contains just #answer and raise an exception.
    def clean(self):
        form_data = self.cleaned_data
        choice_one = str(form_data['choice_one'])
        choice_two = str(form_data['choice_two'])
        choice_three = str(form_data['choice_three'])
        choice_four = str(form_data['choice_four'])
        answer_count = 0
        if choice_one.endswith('#answer'):
            answer_count += 1
        if choice_two.endswith('#answer'):
            answer_count += 1
        if choice_three.endswith('#answer'):
            answer_count += 1
        if choice_four.endswith('#answer'):
            answer_count += 1
        if not answer_count == 1:
            raise ValidationError('A question should have one answer, not less, not more!')

        if choice_one == '#answer' or choice_two == '#answer' or choice_three == '#answer' or choice_four == '#answer':
            raise ValidationError('Define answer before using "#answer"!')
