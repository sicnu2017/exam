"""Exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import  TemplateView
import  xadmin

from users.views import LoginView
from teacher.views import ItemBankView
from teacher.views import GradeCountView,GradeCountIndexView
from student.views import ExamView
from student.views import ExamTestingView
from teacher.views import SetExamView
from users.views import UpdataInfoView
from student.views import GradeSearchView
from teacher.views import MarkingView,AddNewExamView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls, name = "xadmin"),

    url('^$', TemplateView.as_view(template_name = "exam/shouye.html"), name = "shouye"),
    url('^login/$', LoginView.as_view(),name = "login"),
    url(r'^captcha/', include('captcha.urls')),
    url('^item-bank/(?P<type>[0-9])/(?P<course_id>[0-9])/$',ItemBankView.as_view() , name="item-bank"),
    url('^grade-count/(?P<course_id>[0-9])/$',GradeCountView.as_view() , name="grade-count"),
    url('^grade-index/(?P<exam_id>[0-9]{7})/$',GradeCountIndexView.as_view() , name="grade-index"),
    url('^exam/$',ExamView.as_view() , name="exam"),
    url('^testing/$',ExamTestingView.as_view() , name="testing"),
    url('^setExam/$',SetExamView.as_view() , name="setExam"),
    url('^update-info/$',UpdataInfoView.as_view() , name="update-info"),
    url('^grade-search/$',GradeSearchView.as_view() , name="grade-search"),
    url('^marking/$',MarkingView.as_view() , name="marking"),
    url('^addNewExam/$',AddNewExamView.as_view() , name="addNewExam"),

]
