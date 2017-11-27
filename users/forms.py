# _*_ coding:utf-8 _*_
__author__ = 'yancy'
__date__ = '2017/10/31 19:37'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True) #如果字段为空就报错,必填
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(required=True,error_messages={'invalid':u"验证码错误"})










