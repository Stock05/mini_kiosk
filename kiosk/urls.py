from django.urls import path

from . import views
app_name = "kiosk"


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('order/', views.OrderView.as_view(), name="order"),
    
]