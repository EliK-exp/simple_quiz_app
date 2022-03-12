from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    # category = models.ManyToManyField(Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # is_multi_answer = models.BooleanField(default=False)
    def __str__(self):
        return self.question_text


# check if the question has any other answers! A question must have only a single answer.
def validate_answer_text(answer_text):
    print('validating...')
    if str(answer_text)[0].islower():
        raise ValidationError('Start your answer with upper case.')


class Answer(models.Model):
    answer_text = models.CharField(max_length=255, validators=[validate_answer_text])
    is_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    # Check if the question has already an answer. Also avoids the number of answers exceeds from 4.
    def clean(self):
        the_question = self.question
        if the_question.answer_set.filter(is_answer=True).count() > 0 and self.is_answer == True:
            raise ValidationError('this question has already an answer!')
        if the_question.answer_set.count() == 4:
            raise ValidationError('this question has already 4 answers and does not accept answers anymore!')
