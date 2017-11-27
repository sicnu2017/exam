# _*_ encoding:utf-8 _*_
from django.shortcuts import render


from django.views.generic import  View
# Create your views here.
from .models import MchoiceProfile
class ItemBankView(View):
    def get(self,request):
        mchocies = MchoiceProfile.objects.all()
        return render(request, "exam/item-bank.html", {
            'mchoices':mchocies
        })

class GradeCountView(View):
    def get(self,request):
        return render(request, "exam/grade-count.html")



