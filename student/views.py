from django.shortcuts import render
from django.views.generic import  View


from users.models import UserProfile
from teacher.models import ExamProfile
from teacher.models import CourseProfile
from student.models import StudentExam

# Create your views here.

class ExamView(View):
    def get(self,request):
        if request.user.is_authenticated():
            examid = StudentExam.objects.filter(user_id=request.user.id).order_by("add_time")[:1]
            exam_profile = ExamProfile.objects.filter(id = examid)
            return render(request, "exam/exam.html",{'exam_profile':exam_profile})

class ExamTestingView(View):
    def get(self,request):
        return render(request, "exam/testing.html")

class GradeSearchView(View):
    def get(self,request):
        return render(request, "exam/grade-search.html")
