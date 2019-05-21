from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.views import View 
from .models import Student 
from .forms import StudentForm 
# Create your views here.

def index(request):
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return  render(request, 'student/index.html', context=context)

class IndexView(View):
    template_name = 'student/index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
                'studennts': students
        }
        return context

    def get(self, request):
        context =self.get_context()
        form = StudentForm()
        context.update({
            'form':form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:index'))
        context = self.get_context()
        context.update({'form':form})
        return render(request, self.template_name, context=context)

