from django.shortcuts import render
from .models import Choice, Question
from django.views.generic import ListView


# Create your views here.
class IndexView(ListView):
    model = Question
    template_name = "kiosks/index.html"    

  
