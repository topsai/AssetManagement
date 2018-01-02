from django.shortcuts import render
import requests
from plugs import jenkins_plug
# import paramiko
import configparser
from configparser import ConfigParser
from io import StringIO
# import nginx


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
    conf_dict = {'global': {}, 'events': {}, 'http': {}}
    conf_key = 'global'
    with open(file, 'r') as f:
        for i in f:
            print(conf_key)
            line = i.strip().strip(';')
            # 去除已注释配置
            if line.startswith('#'):
                continue
            # 去除注释并分割成两段
            line = line.split('#')[0].strip().strip(';').split(' ', 1)
            # 去除无效行
            if line == ['']:
                continue
            if line == ['events', '{']:
                conf_key = 'events'
                continue
            if line == ['http', '{']:
                conf_key = 'http'
                continue
            if line == ['}']:
                conf_key = 'global'
                continue

            conf_dict[conf_key][line[0]] = line[1]

    return conf_dict


# 创建配置文件
def create_config(conf_dict):
    conf = ''
    for k, v in conf_dict['global'].items():
        str = k + ' ' + v + ';\n'
        conf += str
    conf += 'events {\n'
    for k, v in conf_dict['events'].items():
        str = k + ' ' + v + ';\n'
        conf += str
    conf += '}\n'
    conf += 'http {\n'
    for k, v in conf_dict['http'].items():
        str = k + ' ' + v + ';\n'
        conf += str
    conf += '}\n'
    return conf


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
    conf_dict = cut_conf('/etc/nginx/nginx.conf')
    print(conf_dict)
    data = {'conf': conf_dict}
    ret = create_config(cc)
    print(ret)
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
