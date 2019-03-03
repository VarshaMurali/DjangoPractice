from django.db import models
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=50)
    department_head = models.CharField(max_length=100)
    total_students = models.IntegerField()
    duration = models.IntegerField()
    def __str__(self):
        return self.department_name
    def get_absolute_url(self):
        return reverse ('registry:departmentlist')
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.teacher_name
    def get_absolute_url(self):
        return reverse ('registry:teacherlist')
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    rank = models.IntegerField()
    department = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.student_name
    def get_absolute_url(self):
        return reverse ('registry:studentlist')
