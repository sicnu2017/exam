from django.db import models
from datetime import datetime

from users.models import UserProfile
from teacher.models import ExamProfile

# Create your models here.

class StudentExam(models.Model):
    exam_id = models.ForeignKey(ExamProfile, verbose_name=u'考试ID')
    user_id = models.ForeignKey(UserProfile, verbose_name=u'参考学生ID')
    is_completed = models.BooleanField(default=False, verbose_name=u'考试是否完成')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        db_table = u"StudentExam"
        verbose_name = u"学生考试关联表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.exam_id
