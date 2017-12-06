from django.db import models


from django.db import models


from users.models import UserProfile
from teacher.models import ExamProfile

# Create your models here.

class StudentExam(models.Model):
    exam_id = models.ForeignKey(ExamProfile, verbose_name=u'考试ID')
    user_id =models.ForeignKey(UserProfile, verbose_name=u'参考学生ID')

    class Meta:
        db_table = u"StudentExam"
        verbose_name = u"学生考试关联表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.subject
