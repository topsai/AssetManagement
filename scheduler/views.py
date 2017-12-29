from django.shortcuts import render
import requests
from plugs import jenkins_plug
# import paramiko
import configparser
from configparser import ConfigParser
from io import StringIO


# from ConfigParser import ConfigParser
# 配置文件类
class config:
    def __init__(self):
        self.user = None

    def global_conf(self):
        user = 'www-data'
        worker_processes = 'auto'
        pid = '/run/nginx.pid'
        include = '/etc/nginx/modules-enabled/*.conf'

    def events(self):
        worker_connections = 768
        multi_accept = 'on'

    def http(self):
        pass

# 切配置文件
def cut_conf(file):
    conf_dict = []
    with open(file, 'r') as f:
        for i in f:
            line = i.strip().strip(';')
            # 去除已注释配置
            if line.startswith('#'):
                continue
            line = line.split()
            # 去除无效行
            if len(line) < 2:
                continue
            print(len(line))
            conf_dict.append(line)
    return conf_dict


# Create your views here.
# 调度器管理
def nginx(request):
    cf = configparser.ConfigParser()
    # 建立一个sshclient对象
    # ssh = paramiko.SSHClient()
    # # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # # 调用connect方法连接服务器
    # ssh.connect(hostname='192.168.202.143', port=22, username='root', password='cai@521131')
    # stdin, stdout, stderr = ssh.exec_command('cat /etc/nginx/nginx.conf')
    # # 结果放到stdout中，如果有错误将放到stderr中
    # ssh_ret = stdout.read().decode()
    # print('config:', ssh_ret)
    # 关闭连接
    # ssh.close()
    conf_file = '/etc/nginx/nginx.conf'
    conf = cut_conf(conf_file)
    print('conf:', conf)

    # client = docker.APIClient(base_url='http://192.168.202.143:2375')
    ret = requests.get('http://192.168.202.143:18099/nginx_status')
    # data = models.User.objects.all()
    ret = ret.text.split()
    ret = [ret[2], ret[7], ret[8], ret[9], ret[11], ret[13], ret[15]]
    server = jenkins_plug.MyJenkins()
    server.conn()
    count = None
    svncount = server.getsvnnum('test', 44)
    return render(request, 'sb-admin/pages/scheduler/nginx.html',
                  {'ret': ret, 'count': count, 'svncount': None, 'ssh_ret': conf})
