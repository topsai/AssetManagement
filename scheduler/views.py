from django.shortcuts import render, HttpResponse
import requests
from plugs import jenkins_plug
import paramiko
from django.conf import settings
import configparser
from configparser import ConfigParser
from io import StringIO
import re


# import nginx

def get_info(cmd):
    ret = None
    err = None
    ssh = paramiko.SSHClient()
    print('get info {}'.format(cmd))
    try:
        trans = paramiko.Transport((settings.DOCKER_SERVER, 22))
        trans.connect(username='root', password='Dtma@2018')
        ssh._transport = trans
        stdin, ret, err = ssh.exec_command(cmd)
        ret = ret.read().decode()
        err = err.read().decode()
    except Exception as e:
        print('ssh err:', e)
    finally:
        ssh.close()

    return ret, err


# from ConfigParser import ConfigParser
from plugs.conf_plug import cut_conf, create_config, cut_conf1


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
    conf_dict = {}
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
    nginx1 = nginx1.read().decode()
    print('nginx1:', nginx1)
    # 匹配配置内容
    # re.match("(\w+)\s+([^;]+)", a)
    # TODO 下一版本改为正则表达式匹配每一项
    if nginx1:
        for i in nginx1.split('\n'):
            ret = re.match("(\w+)\s+([^;]+)", i)
            try:
                k, v = ret.groups()
                conf_dict[k] = v
            except:
                pass

    # 执行命令
    # stdin, stdout, stderr = ssh.exec_command('netstat -apn | grep nginx')
    # # 结果放到stdout中，如果有错误将放到stderr中

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


def server(request, conf=None):
    data = {}
    if conf:
        cmd = 'cat {}{}'.format(settings.CONF_DIR, conf)
        ret, err = get_info(cmd)
        data['ret'] = ret
        return HttpResponse(ret)
    conf_list = []
    if request.method == 'POST':
        server_name = request.POST.get('server_name')
        listen = request.POST.get('listen')
        location = request.POST.get('location')
        root = request.POST.get('root')
        index = request.POST.get('index')
        conf = "server {server_name %s;\nlisten %s;\nlocation %s \n{root %s;\nindex %s;\n}\n}\n" % (
            server_name, listen, location, root, index)
        cmd = 'echo "{}" >>{}{}.conf'.format(conf, settings.CONF_DIR, server_name)
        print('cmd:', cmd)
        ret, err = get_info(cmd)
        print('ret:', ret.read().decode())
        print('err:', err.read().decode())

    # elif request.method == 'GET':

    confs, stderr = get_info('ls {}'.format(settings.CONF_DIR))
    if confs:
        for i in confs.split('\n'):
            if len(i) > 5:
                conf_list.append(i)
    else:
        print('e', stderr)
    data['confs'] = conf_list
    return render(request, 'sb-admin/pages/scheduler/server.html', data)


def nginx_test():
    cmd = 'nginx -t'
    ret, err = get_info(cmd)
    return ret, err


def upstream(request):
    return render(request, 'sb-admin/pages/scheduler/upstream.html')
