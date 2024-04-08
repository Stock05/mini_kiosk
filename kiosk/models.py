from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    drinks_type = models.CharField(max_length=200)    
    def __str__(self):
        text = self.drinks_type 
        return text    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)    

    def __str__(self):        
        return self.drink_name
   

class Order(models.Model):
    order_id = models.IntegerField()
    order_menu = models.CharField(max_length=200)
    order_count = models.IntegerField(default=0)
    order_price = models.IntegerField(default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)  # 주문 연결 ( ForeignKey )
    drink = models.ForeignKey(Choice, on_delete=models.CASCADE)  # 음료 연결 ( ForeignKey )
    quantity = models.IntegerField()  # 주문 수량
    price = models.IntegerField()  # 가격

    def __str__(self):
        return f"{self.drink.drink_name} ({self.quantity}개)"