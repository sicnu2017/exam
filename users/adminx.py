# _*_ coding:utf-8 _*_
__author__ = 'yancy'
__date__ = '2017/10/18'

import xadmin
from xadmin import views
from django.contrib.auth.models import AbstractUser


from .models import UserProfile
from .models import DeptProfile




#全局设置
class BaseSetting(object):
    enable_themes = True #修改页面风格
    use_bootswatch = True

 #修改一些标题
class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'Exam_Online'
    # 设置base_site.html的Footer
    site_footer  = 'Sicnu'
    menu_style = "accordion"#折叠列表default,accordion

class DeptProfileAdmin(object): #部门信息展示列
    list_display = ('deptname', 'deptlevel', 'parentid', 'is_active', 'add_time')  # 显示列信息
    search_fields = ('deptname', 'deptlevel', 'parentid', 'is_active')  # 添加搜索栏
    list_filter = ('deptname', 'deptlevel', 'parentid', 'is_active', 'add_time')  # 显示过滤器
    model_icon = 'fa fa-user' #图标

class UserProfileAadmin(object): #人员信息展示列
    list_display = ('deptname', 'deptlevel', 'parentid', 'is_active', 'add_time')  # 显示列信息
    search_fields = ('deptname', 'deptlevel', 'parentid', 'is_active')  # 添加搜索栏
    list_filter = ('deptname', 'deptlevel', 'parentid', 'is_active', 'add_time')  # 显示过滤器


xadmin.site.register(DeptProfile,DeptProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
