# _*_ encoding:utf-8 _*_
from datetime import datetime


from django.db import models
from users.models import UserProfile



# Create your models here.


#选择题试题表
class MchoiceProfile(models.Model):
    subject = models.CharField(max_length=128, verbose_name=u"题目")
    optionA = models.CharField(max_length=64, verbose_name=u"选项A", blank=True)
    optionB = models.CharField(max_length=64, verbose_name=u"选项B", blank=True)
    optionC = models.CharField(max_length=64, verbose_name=u"选项C", blank=True)
    optionD = models.CharField(max_length=64, verbose_name=u"选项D", blank=True)
    optionE = models.CharField(max_length=64, verbose_name=u"选项E", blank=True)
    answer = models.CharField(max_length=12,verbose_name=u"正确答案", blank=True)
    level = models.CharField(max_length=12,choices=(("simple",u"简单"),("medium",u"中等"),("hard",u"困难")),default='simple',verbose_name=u"难易度")
    value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
    is_multiple = models.BooleanField(default=False, verbose_name=u"是否多选")
    createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        db_table = u"MchoiceProfile"
        verbose_name = u"选择题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
#判断题试题表
# class JudgmentProfile(models.Model):
#     subject = models.CharField(max_length=128, verbose_name=u"题目")
#     answer = models.CharField(max_length=12,choices=(("T",u"正确"),("F",u"错误")), verbose_name=u"难易度", blank=True)
#     level = models.CharField(max_length=12,choices=(("simple",u"简单"),("medium",u"中等"),("hard",u"困难")),default='simple',verbose_name=u"难易度")
#     value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
#     createuser = models.ForeignKey(UserProfile, verbose_name=u"创建人", blank=True)
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
#
#     class Meta:
#         verbose_name = u"判断题"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.subject
# #填空题试题表
# class CompletionProfile(models.Model):
#     subject = models.CharField(max_length=128, verbose_name=u"题目")
#     answerA = models.CharField(max_length=32, verbose_name=u"第一空答案", blank=True)
#     answerB = models.CharField(max_length=32, verbose_name=u"第二空答案", blank=True)
#     level = models.CharField(max_length=12, choices=(("simple", u"简单"), ("medium", u"中等"), ("hard", u"困难")),default='simple', verbose_name=u"难易度")
#     value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
#     createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
#
#     class Meta:
#         verbose_name = u"填空题"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.subject
# #分析题试题表
# class AnalysisProfile(models.Model):
#     subject = models.CharField(max_length=128, verbose_name=u"题目")
#     answer = models.CharField(max_length=128, verbose_name=u"参考答案", blank=True)
#     level = models.CharField(max_length=12, choices=(("simple", u"简单"), ("medium", u"中等"), ("hard", u"困难")),default='simple', verbose_name=u"难易度")
#     value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
#     createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
#
#     class Meta:
#         verbose_name = u"分析题"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.subject
