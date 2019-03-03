from django.contrib import admin
from django.conf.urls import url
from registry import views

app_name='registry'

urlpatterns = [
  url(r'^$',views.index,name='index'),

  url(r'^teacherlist/(?P<pk>\d+)/$',views.TeacherDetail.as_view(),name='teacherdetail'),
  url(r'^teacherlist/delete/(?P<pk>\d+)/$',views.TeacherDelete.as_view(),name='deleteteacher'),
  url(r'^teacherlist/update/(?P<pk>\d+)/$',views.TeacherUpdate.as_view(),name='updateteacher'),
  url(r'^teacherlist/create/$',views.TeacherCreate.as_view(),name='newteacher'),
  url(r'^teacherlist/$',views.TeacherList.as_view(),name='teacherlist'),

  url(r'^studentlist/(?P<pk>\d+)/$',views.StudentDetail.as_view(),name='studentdetail'),
  url(r'^studentlist/update/(?P<pk>\d)/$',views.StudentUpdate.as_view(),name='updatestudent'),
  url(r'^studentlist/delete/(?P<pk>\d)/$',views.StudentDelete.as_view(),name='deletestudent'),
  url(r'^studentlist/create/$',views.StudentCreate.as_view(),name='newstudent'),
  url(r'^studentlist/$',views.StudentList.as_view(),name='studentlist'),

  url(r'^departmentlist/(?P<pk>[\d+])$',views.DepartmentDetail.as_view(),name='departmentdetail'),
  url(r'^departmentlist/update/(?P<pk>\d)/$',views.DepartmentUpdate.as_view(),name='updatedepartment'),
  url(r'^departmentlist/delete/(?P<pk>\d)/$',views.DepartmentDelete.as_view(),name='deletedepartment'),
  url(r'^departmentlist/create/$',views.DepartmentCreate.as_view(),name='newdepartment'),
  url(r'^departmentlist/',views.DepartmentList.as_view(),name='departmentlist'),
]
