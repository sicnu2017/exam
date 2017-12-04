from django.shortcuts import render
from django.views.generic import  View

# Create your views here.

class ExamView(View):
    def get(self,request):
        return render(request, "exam/exam.html")

class ExamTestingView(View):
    def get(self,request):
        return render(request, "exam/testing.html")

class GradeSearchView(View):
    def get(self,request):
        return render(request, "exam/grade-search.html")
