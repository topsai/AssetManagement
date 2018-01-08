from django.db import models


# Create your models here.
from django.db.transaction import on_commit


# 用户
class User(models.Model):
    name = models.CharField(max_length=256)
    department = models.ForeignKey('DepartmentType')
    devices = models.ManyToManyField(to='ComputerInfo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '用户'


# 电脑信息
class ComputerInfo(models.Model):
    model = models.CharField(max_length=256)
    sn = models.CharField(max_length=256, blank=True)
    type = models.ForeignKey('ComputerType')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = '电脑信息'


# 电脑类习惯
class ComputerType(models.Model):
    name = models.CharField(max_length=256)
    comments = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '电脑类型'


# 部门
class DepartmentType(models.Model):
    name = models.CharField(max_length=256)
    comments = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '部门'


# 服务器
class Server(models.Model):
    name = models.CharField(max_length=256)
    ip = models.GenericIPAddressField()
    type = models.ForeignKey('ServerType')

    def __str__(self):
        return self.name


# 服务器类型
class ServerType(models.Model):
    name = models.CharField(max_length=256)
    comments = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '服务器类型'
