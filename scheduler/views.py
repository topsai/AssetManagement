from django.shortcuts import render
import requests
from plugs import jenkins_plug


# Create your views here.
# 调度器管理
def nginx(request):
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
                  {'ret': ret, 'count': count, 'svncount': svncount})
