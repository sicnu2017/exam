# _*_ encoding:utf-8 _*_
from datetime import datetime


from django.db import models
from users.models import UserProfile




# Create your models here.

class CourseProfile(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        db_table = u"CourseProfile"
        verbose_name = u"课程名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


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
    createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
    course = models.ForeignKey(CourseProfile, blank=True, verbose_name=u"课程名")

    class Meta:
        db_table = u"MchoiceProfile"
        verbose_name = u"选择题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


#判断题试题表
class JudgmentProfile(models.Model):
    subject = models.CharField(max_length=128, verbose_name=u"题目")
    answer = models.CharField(max_length=12,choices=(("T",u"正确"),("F",u"错误")), verbose_name=u"难易度", blank=True)
    level = models.CharField(max_length=12,choices=(("simple",u"简单"),("medium",u"中等"),("hard",u"困难")),default='simple',verbose_name=u"难易度")
    value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
    createuser = models.ForeignKey(UserProfile, verbose_name=u"创建人", blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
    course = models.ForeignKey(CourseProfile, blank=True, verbose_name=u"课程名")
    class Meta:
        db_table = u"JudgmentProfile"
        verbose_name = u"判断题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


# 填空题试题表
class CompletionProfile(models.Model):
     subject = models.CharField(max_length=128, verbose_name=u"题目")
     answerA = models.CharField(max_length=32, verbose_name=u"第一空答案", blank=True)
     answerB = models.CharField(max_length=32, verbose_name=u"第二空答案", blank=True)
     level = models.CharField(max_length=12, choices=(("simple", u"简单"), ("medium", u"中等"), ("hard", u"困难")),default='simple', verbose_name=u"难易度")
     value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
     createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
     course = models.ForeignKey(CourseProfile, blank=True, verbose_name=u"课程名")

     class Meta:
         db_table = u"CompletionProfile"
         verbose_name = u"填空题"
         verbose_name_plural = verbose_name

     def __str__(self):
         return self.subject


class AnalysisProfile(models.Model):
    subject = models.CharField(max_length=128, verbose_name=u"题目")
    answer = models.CharField(max_length=128, verbose_name=u"参考答案", blank=True)
    level = models.CharField(max_length=12, choices=(("simple", u"简单"), ("medium", u"中等"), ("hard", u"困难")),default='simple', verbose_name=u"难易度")
    value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
    createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
    course = models.ForeignKey(CourseProfile, blank=True, verbose_name=u"课程名")
    class Meta:
        db_table = u"AnalysisProfile"
        verbose_name = u"分析题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


#多选择题试题表
class MoremchoiceProfile(models.Model):
    subject = models.CharField(max_length=128, verbose_name=u"题目")
    optionA = models.CharField(max_length=64, verbose_name=u"选项A", blank=True)
    optionB = models.CharField(max_length=64, verbose_name=u"选项B", blank=True)
    optionC = models.CharField(max_length=64, verbose_name=u"选项C", blank=True)
    optionD = models.CharField(max_length=64, verbose_name=u"选项D", blank=True)
    optionE = models.CharField(max_length=64, verbose_name=u"选项E", blank=True)
    answers = models.CharField(max_length=12,verbose_name=u"正确答案", blank=True)
    level = models.CharField(max_length=12,choices=(("simple",u"简单"),("medium",u"中等"),("hard",u"困难")),default='simple',verbose_name=u"难易度")
    value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=u"分值", blank=True)
    createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")
    course = models.ForeignKey(CourseProfile, blank=True, verbose_name=u"课程名")

    class Meta:
        db_table = u"MoremchoiceProfile"
        verbose_name = u"选择题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject



#试卷信息模型
class TestProfile(models.Model):
    mchoice_id = models.CharField(max_length=128, verbose_name=u'单选题ID', blank= True)
    moremchoice_id = models.CharField(max_length=128, verbose_name=u'多选题ID', blank= True)
    judgment_id = models.CharField(max_length=128, verbose_name=u'判断题ID', blank= True)
    completion_id = models.CharField(max_length=128, verbose_name=u'填空题ID', blank= True)
    analysis_id = models.CharField(max_length=128, verbose_name=u'分析题ID', blank= True)
    create_user = models.ForeignKey(UserProfile, blank=True, verbose_name=u'创建人')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        db_table = u"TestProfile"
        verbose_name = u"试卷信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.id


#每场考试模型
class ExamProfile(models.Model):
    course = models.ForeignKey(CourseProfile, blank=True, verbose_name=u"课程名")
    createuser = models.ForeignKey(UserProfile, blank=True, verbose_name=u"创建人")
    test_id = models.ForeignKey(TestProfile, blank=True, verbose_name=u'试卷ID')
    start_time = models.DateTimeField(blank=True, verbose_name=u'开始时间')
    end_time = models.DateTimeField(blank=True, verbose_name=u'结束时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        db_table = u"ExamProfile"
        verbose_name = u"考试列表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.id






