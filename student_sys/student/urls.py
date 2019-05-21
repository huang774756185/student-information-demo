from django.urls import path
from . import views
from student.views import IndexView
app_name = "student"
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),

]

