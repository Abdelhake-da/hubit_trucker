from django.urls import path
from . import views
app_name = 'userHabit'
urlpatterns = [
    path('', views.index, name='index'),
]