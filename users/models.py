# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


#部门信息
class DeptProfile(models.Model):
    deptname = models.CharField(max_length=50, verbose_name=u"部门名称")
    parentid = models.CharField(max_length=32, verbose_name=u"父节点ID")
    deptlevel = models.SmallIntegerField(verbose_name=u"部门层级")
    is_active = models.BooleanField(default=True,verbose_name=u"是否激活")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"增加时间")

    class Meta:
        verbose_name = u"部门信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.deptname


#继承AbstractBaseUser扩展用户信息表
class UserProfile(AbstractUser):
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="female",verbose_name=u"性别")
    mobile = models.CharField(max_length=11,null= True,blank=True,verbose_name=u"电话号码")
    role = models.CharField(max_length=10,choices=(("student",u"学生"),("teacher",u"教师"),("admin",u"教务管理员")),default='student',verbose_name=u"角色")
    deptname = models.ForeignKey(DeptProfile,default=1,verbose_name=u"部门名称")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self): #python2 __unicode__
        return self.username







