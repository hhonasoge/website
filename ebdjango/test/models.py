from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class OpenQuestion(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    content = models.CharField(max_length=500)
    def __str__self(self):
        return self.name + " " + self.email + " " + self.content

class OpenQuestionForm(ModelForm):
    class Meta:
        model = OpenQuestion
        fields = ['name', 'email', 'content']

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

