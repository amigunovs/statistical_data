from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Statistics_data, name="Canada_stat"),

]
