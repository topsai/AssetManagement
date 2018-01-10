from django.shortcuts import render
import requests
from plugs import jenkins_plug
import paramiko
from django.conf import settings
import configparser
from configparser import ConfigParser
from io import StringIO
# import nginx


# from ConfigParser import ConfigParser
from plugs.conf_plug import cut_conf, create_config, cut_conf1

cc = {'global': {'user': 'www-data', 'worker_processes': 'auto', 'pid': '/run/nginx.pid'},
      'events': {'worker_connections': '768'},
      'http': {'sendfile': 'on', 'tcp_nopush': 'on', 'tcp_nodelay': 'on', 'keepalive_timeout': '65',
               'types_hash_max_size': '2048', 'include': '/etc/nginx/sites-enabled/*',
               'default_type': 'application/octet-stream', 'ssl_protocols': 'TLSv1 TLSv1.1 TLSv1.2',
               'ssl_prefer_server_ciphers': 'on', 'access_log': '/var/log/nginx/access.log',
               'error_log': '/var/log/nginx/error.log', 'gzip': 'on', 'gzip_disable': '"msie6"'}}


# Create your views here.
# 调度器管理
def nginx(request):
    # cf = configparser.ConfigParser()
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
    # conf_file = '/etc/nginx/nginx.conf'
    # conf = cut_conf(conf_file)
    # print('conf:', conf)
    #
    # # client = docker.APIClient(base_url='http://192.168.202.143:2375')
    # ret = requests.get('http://192.168.202.143:18099/nginx_status')
    # # data = models.User.objects.all()
    # ret = ret.text.split()
    # ret = [ret[2], ret[7], ret[8], ret[9], ret[11], ret[13], ret[15]]
    # server = jenkins_plug.MyJenkins()
    # server.conn()
    # count = None
    # svncount = server.getsvnnum('test', 44)
    # data = {'ret': ret, 'count': count, 'svncount': None, 'ssh_ret': conf}
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
    stdin, nginxv1, nginxv = ssh.exec_command('nginx -v')
    stdin, nginx1, stderr = ssh.exec_command('cat /etc/nginx/nginx.conf')
    stdin, confs, stderr = ssh.exec_command('ls /etc/nginx/conf.d/')
    confs = confs.read().decode()
    # 执行命令
    # stdin, stdout, stderr = ssh.exec_command('netstat -apn | grep nginx')
    # # 结果放到stdout中，如果有错误将放到stderr中
    nginx1 = nginx1.read().decode()
    # nginx2 = nginx2.read().decode()
    nginx = nginxv.read().decode().split(':', 1)[1]
    ssh.close()
    import platform
    # print(nginx1)
    system = platform.release()
    # server_type = models.ServerType.objects.all()
    # # fm = forms.ServerTypeForm(initial=server_type)
    # date = {
    #     'jenkins': JENKINS_SERVER,
    #     'docker': DOCKER_SERVER,
    #     'system': system,
    #     'nginx': nginx,
    #     # 'fm': fm,
    # }
    # conf_dict = cut_conf1(nginx1)
    # print(conf_dict)

    data = {
        'conf': nginx1,
        'confs': confs,
    }
    print(nginx1)
    # ret = create_config(cc)
    # print(ret)
    return render(request, 'sb-admin/pages/scheduler/nginx.html', data)


nginx_conf = {
    'user': 'www-data',
    'worker_processes': 'auto',
    'pid': '/run/nginx.pid',
    'events': '{',
    'worker_connections': '768',
    'http': '{',
    'sendfile': 'on',
    'tcp_nopush': 'on',
    'tcp_nodelay': 'on',
    'keepalive_timeout': '65',
    'types_hash_max_size': '2048',
    'http.include.0': '/etc/nginx/mime.types',
    'default_type': 'application/octet-stream',
    'ssl_protocols': 'TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE',
    'ssl_prefer_server_ciphers': 'on',
    'access_log': '/var/log/nginx/access.log',
    'error_log': '/var/log/nginx/error.log',
    'gzip': 'on',
    'gzip_disable': '"msie6"',
    'http.include.1': '/etc/nginx/conf.d/*.conf',
    'http.include.2': '/etc/nginx/sites-enabled/*',
}
