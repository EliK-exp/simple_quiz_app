from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    # category = models.ManyToManyField(Category)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # is_multi_answer = models.BooleanField(default=False)


class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    is_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
