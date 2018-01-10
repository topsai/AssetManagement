from django.shortcuts import render
from pc_manage import models
from plugs.jenkins_plug import MyJenkins
from django.conf import settings
from plugs import paramiko_plug
import jenkins
import requests
import docker
import paramiko
import time
import forms


# Create your views here.
def index(request):
    client = docker.APIClient(base_url='http://192.168.202.143:2375')
    # ret = requests.get('http://192.168.202.143:18099/nginx_status')
    # ret = []
    # data = models.User.objects.all()
    # ret = ret.text.split()
    # ret = [ret[2], ret[7], ret[8], ret[9], ret[11], ret[13], ret[15]]
    # server = MyJenkins()
    # server.conn()
    # count = None
    # svncount = None
    data = {}
    # {'data': data, 'ret': ret, 'count': count, 'svncount': svncount}
    return render(request, 'sb-admin/pages/index.html', )


# 自动发布
def AutoReleased(request):
    return render(request, '')


# 电脑管理
def pc(request):
    data = models.User.objects.all()
    return render(request, 'pc.html', {'data': data})


# 服务器管理
def server(request):
    JENKINS_SERVER = settings.JENKINS_SERVER
    DOCKER_SERVER = settings.DOCKER_SERVER
    # ssh = paramiko.SSHClient()
    # # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # # 调用connect方法连接服务器
    # ssh.connect(hostname=DOCKER_SERVER, port=22, username='root', password='Dtma@2018')
    # stdin, stdout, stderr = ssh.exec_command('nginx -v')
    # # 结果放到stdout中，如果有错误将放到stderr中
    # print(stdout.read().decode())

    trans = paramiko.Transport((DOCKER_SERVER, 22))
    # 建立连接
    trans.connect(username='root', password='Dtma@2018')

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    # 执行命令，和传统方法一样
    stdin, stdout, stderr = ssh.exec_command('nginx -v')
    # 执行命令
    # stdin, stdout, stderr = ssh.exec_command('netstat -apn | grep nginx')
    # # 结果放到stdout中，如果有错误将放到stderr中
    nginx =stderr.read().decode().split(':', 1)[1]
    ssh.close()
    import platform
    print(nginx)
    system = platform.release()
    server_type = models.ServerType.objects.all()
    # fm = forms.ServerTypeForm(initial=server_type)
    date = {
        'jenkins': JENKINS_SERVER,
        'docker': DOCKER_SERVER,
        'system': system,
        'nginx': nginx,
        # 'fm': fm,
    }
    return render(request, 'sb-admin/pages/server.html', date)
