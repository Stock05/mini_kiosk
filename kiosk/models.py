from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    drinks_type = models.CharField(max_length=200)    
    def __str__(self):
        text = self.question_text 
        return text    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    def __str__(self):        
        return self.choice_text