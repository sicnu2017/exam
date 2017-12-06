# _*_ encoding:utf-8 _*_
from django.shortcuts import render


from django.views.generic import  View
# Create your views here.
from .models import MchoiceProfile,MoremchoiceProfile,JudgmentProfile,CompletionProfile,AnalysisProfile,CourseProfile
from .models import ExamProfile,ExamGradeCountProfile

#测试
class ItemBankView(View):
    def get(self,request,type,course_id):
        course = CourseProfile.objects.filter(id=course_id)
        if type == '1' :
            mchocies = MchoiceProfile.objects.filter(course = course_id)
            questionType = '选择题'
        elif type == '2':
            mchocies = MoremchoiceProfile.objects.filter(course = course_id)
            questionType = '多选题'
        elif type == '3':
            mchocies = JudgmentProfile.objects.filter(course = course_id)
            questionType = '判断题'
        elif type == '4':
            mchocies = CompletionProfile.objects.filter(course = course_id)
            questionType = '填空题'
        else:
            mchocies = AnalysisProfile.objects.filter(course = course_id)
            questionType = '分析题'
        courses = CourseProfile.objects.all()

        return render(request, "exam/item-bank.html", {
            'mchoices':mchocies,
            'course_id':course_id,
            'questionType':questionType,
            'courses':courses,
            'course_name':course[0].name
        })

class GradeCountView(View):
    def get(self,request,course_id):
        if course_id == '0':
            exams = ExamProfile.objects.all()
        else:
            exams = ExamProfile.objects.filter(course = course_id)
        courses = CourseProfile.objects.exclude(id = course_id)
        course = CourseProfile.objects.filter(id = course_id)
        return render(request, "exam/grade-count.html",{
            'courses': courses,
            'exams':exams,
            'course_name':course[0].name
        })

class GradeCountIndexView(View):
    def get(self,request,exam_id):
        exams = ExamGradeCountProfile.objects.filter(exam_id = exam_id)
        return render(request, "exam/grade-count-index.html",{
            'exams':exams,
        })

class SetExamView(View):
    def get(self,request):
        return render(request, "exam/setExam.html")

class MarkingView(View):
    def get(self,request):
        return render(request, "exam/marking.html")

class AddNewExamView(View):
    def get(self,request):
        return render(request, "exam/addNewExam.html")