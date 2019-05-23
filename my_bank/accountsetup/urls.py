from django.conf.urls import url
from django.urls import path,include
from accountsetup import views

app_name='accountsetup'

urlpatterns = [
#url(r'^$',views.index,name='index'),
url(r'^$',views.AccountApi.as_view()),
#url(r'^accountlist/(?P<pk>\d+)$/',views.deposit,name='depositamount')
url(r'^(?P<pk>\d+)/$',views.Accountdetail.as_view()),

]
'''
urlpatterns = [
#path('',views.AccountList.as_view(),name='accountlist') ,
path('',views.AccountApi.as_view()),
path('<int:pk>/',views.Accountdetail.as_view()),
path('accountlist/<int:pk>/deposit/',views.depositamount,name='depositamount'),
path('accountlist/<int:pk>/withdraw/',views.withdrawamount,name='withdrawamount'),
]
'''
