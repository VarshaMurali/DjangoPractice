from django.shortcuts import render
from django.urls import reverse_lazy
from registry import models
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)

# Create your views here.

def index(request):
    return render(request,"registry/base.html")

class TeacherList(ListView):
    context_object_name='teachers'
    model= models.Teacher
    template_name='registry/teacherlist.html'
class TeacherDetail(DetailView):
    context_object_name='teacher'
    model=models.Teacher
    template_name='registry/teacherdetail.html'
class TeacherCreate(CreateView):
    fields = ('teacher_name','qualification','department')
    model = models.Teacher
class TeacherUpdate(UpdateView):
    fields = ('teacher_name','qualification','department')
    model =  models.Teacher
class TeacherDelete(DeleteView):
    model = models.Teacher
    success_url = reverse_lazy('registry:teacherlist')

class StudentList(ListView):
    context_object_name='students'
    model=models.Student
    template_name='registry/studentlist.html'
class StudentDetail(DetailView):
    contxt_object_name='student'
    model=models.Student
    template_name='registry/studentdetail.html'
class StudentCreate(CreateView):
    fields = ('student_name','rank','department')
    model = models.Student
class StudentUpdate(UpdateView):
    fields = ('student_name','rank','department')
    model = models.Student
class StudentDelete(DeleteView):
    model = models.Student
    success_url = reverse_lazy('registry:studentlist')

class DepartmentList(ListView):
    context_object_name='departments'
    model=models.Department
    template_name='registry/departmentlist.html'
class DepartmentDetail(DetailView):
    context_object_name='department'
    model=models.Department
    template_name='registry/departmentdetail.html'
class DepartmentCreate(CreateView):
    fields = ('department_name','department_head','total_students','duration')
    model=models.Department
class DepartmentUpdate(UpdateView):
    fields = ('department_name','department_head','total_students','duration')
    model=models.Department
class DepartmentDelete(DeleteView):
    model=models.Department
    success_url= reverse_lazy('registry:departmentlist')
