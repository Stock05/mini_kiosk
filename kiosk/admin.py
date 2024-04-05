from django.contrib import admin
from kiosk.models import Question,Choice
# Register your models here.


@admin.register(Question)
class KioskAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class KioskAdmin(admin.ModelAdmin):
    list_display=('question','drink_name','price')

