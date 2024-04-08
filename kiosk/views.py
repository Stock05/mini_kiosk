from django.shortcuts import render, redirect
from .models import Choice, Question, OrderItem
from django.views.generic import ListView


# Create your views here.
class IndexView(ListView):
    model = Question
    template_name = "kiosks/index.html"    

  
class OrderView(ListView):
    model = Question
    template_name = "kiosks/order.html"    


