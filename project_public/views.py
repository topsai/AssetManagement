from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from plugs.jenkins_plug import MyJenkins
from bs4 import BeautifulSoup
import requests
import time
from requests.auth import HTTPBasicAuth
from django.conf import settings


# 获取进度条
def build_bar(job_name):
    server = MyJenkins()
    server.conn()
    url = 'http://192.168.4.241/jenkins/job/lastBuild/lastBuild/api/xml?depth=1'.format(job_name)
    a = server.get_build_info(name, number, depth=0)
    ret = requests.get(url)
    soup = BeautifulSoup(url)


# Create your views here.
def new_oa(request):
    auth = HTTPBasicAuth('admin', 'admin')
    # ret = requests.get('http://192.168.202.143:18099/nginx_status')
    ret = None
    url = 'http://{}/jenkins/job/test/lastBuild/api/json?depth=1'.format(settings.JENKINS_SERVER)
    t = requests.get(url, auth=('admin', 'admin'))
    # data = models.User.objects.all()
    # ret = ret.text.split()
    # ret = [ret[2], ret[7], ret[8], ret[9], ret[11], ret[13], ret[15]]
    server = MyJenkins()
    server.conn()
    build_history = []
    # 获取构建历史
    job_info = server.server.get_job_info('test', 1)
    # 重新组织 构建历史 数据
    for i in job_info['builds'][:10]:
        build_history.append(
            [i['displayName'], time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(i['timestamp'] / 1000)), i['result'], i['number']])

    job_info = None
    count = None
    svncount = None
    data = {
        'ret': ret,
        'count': count,
        'svncount': svncount,
        'job_info': job_info,
        'build_history': build_history,
    }
    return render(request, 'sb-admin/pages/project_public/new_oa.html', data)


def xinlianpu(request):
    print('xinlianpu')
    return render(request, 'sb-admin/pages/project_public/xinlianpu.html')


@csrf_exempt
def buildinfo(request):
    print(request)
    if request.method == 'POST':
        print(request.POST)
        print(request.body)

    return HttpResponse('ok')


# 获取构建输出信息
def get_build_console(request, job_name, number):
    server = MyJenkins()
    server.conn()
    data = server.server.get_build_console_output(job_name, int(number)).replace('\n', '<br>')
    print(data)
    return HttpResponse(data)


ss = \
    {
        '_class': 'hudson.maven.MavenModuleSet',
        'actions': [None, {}, {}, {'_class': 'com.cloudbees.plugins.credentials.ViewCredentialsAction', 'stores': {}}],
        'description': '',
        'displayName': 'test',
        'displayNameOrNull': None,
        'fullDisplayName': 'test',
        'fullName': 'test',
        'name': 'test',
        'url': 'http://192.168.4.241/jenkins/job/test/',
        'buildable': True,
        'builds': [
            {
                '_class': 'hudson.maven.MavenModuleSetBuild',
                'actions': [{'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                            {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}],
                'artifacts': [],
                'building': False,
                'description': None,
                'displayName': '#46',
                'duration': 147382,
                'estimatedDuration': 134177,
                'executor': None,
                'fullDisplayName': 'test #46',
                'id': '46',
                'keepLog': False,
                'number': 46,
                'queueId': 47,
                'result': 'SUCCESS',
                'timestamp': 1514342734339,
                'url': 'http://192.168.4.241/jenkins/job/test/46/',
                'builtOn': '',
                'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet',
                    'items': [],
                    'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]
                },
                'culprits': [],
                'mavenArtifacts': {},
                'mavenVersionUsed': '3.5.2'
            },
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#45', 'duration': 118129, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #45', 'id': '45', 'keepLog': False, 'number': 45, 'queueId': 46,
             'result': 'SUCCESS', 'timestamp': 1514300698335, 'url': 'http://192.168.4.241/jenkins/job/test/45/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user admin',
                                                                             'userId': 'admin', 'userName': 'admin'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#44', 'duration': 137019, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #44', 'id': '44', 'keepLog': False, 'number': 44, 'queueId': 45,
             'result': 'SUCCESS', 'timestamp': 1514300210919, 'url': 'http://192.168.4.241/jenkins/job/test/44/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user admin',
                                                                             'userId': 'admin', 'userName': 'admin'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#43', 'duration': 109996, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #43', 'id': '43', 'keepLog': False, 'number': 43, 'queueId': 44,
             'result': 'SUCCESS', 'timestamp': 1514297999693, 'url': 'http://192.168.4.241/jenkins/job/test/43/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user admin',
                                                                             'userId': 'admin', 'userName': 'admin'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#42', 'duration': 142773, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #42', 'id': '42', 'keepLog': False, 'number': 42, 'queueId': 43,
             'result': 'SUCCESS', 'timestamp': 1514297343219, 'url': 'http://192.168.4.241/jenkins/job/test/42/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user admin',
                                                                             'userId': 'admin', 'userName': 'admin'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {
                                                                           '_class': 'jenkins.model.InterruptedBuildAction'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#41', 'duration': 93570, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #41', 'id': '41', 'keepLog': False, 'number': 41, 'queueId': 42,
             'result': 'ABORTED', 'timestamp': 1514297227747, 'url': 'http://192.168.4.241/jenkins/job/test/41/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user admin',
                                                                             'userId': 'admin', 'userName': 'admin'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {
                                                                           '_class': 'jenkins.model.InterruptedBuildAction'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#40', 'duration': 67275, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #40', 'id': '40', 'keepLog': False, 'number': 40, 'queueId': 41,
             'result': 'ABORTED', 'timestamp': 1514297074427, 'url': 'http://192.168.4.241/jenkins/job/test/40/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user admin',
                     'userId': 'admin', 'userName': 'admin'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'jenkins.model.InterruptedBuildAction'}, {}, {}], 'artifacts': [], 'building': False,
                                            'description': None, 'displayName': '#39', 'duration': 53194,
                                            'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #39', 'id': '39', 'keepLog': False, 'number': 39,
                                            'queueId': 40, 'result': 'ABORTED', 'timestamp': 1514296947986,
                                            'url': 'http://192.168.4.241/jenkins/job/test/39/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': None,
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user admin',
                                                                                    'userId': 'admin',
                                                                                    'userName': 'admin'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#38', 'duration': 142594,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #38', 'id': '38',
                                                                           'keepLog': False, 'number': 38,
                                                                           'queueId': 39, 'result': 'SUCCESS',
                                                                           'timestamp': 1514270213439,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/38/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user admin',
                                                                             'userId': 'admin', 'userName': 'admin'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#37', 'duration': 221597, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #37', 'id': '37', 'keepLog': False, 'number': 37, 'queueId': 38,
             'result': 'SUCCESS', 'timestamp': 1514258985178, 'url': 'http://192.168.4.241/jenkins/job/test/37/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#36',
                                            'duration': 157873, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #36', 'id': '36', 'keepLog': False, 'number': 36,
                                            'queueId': 37, 'result': 'SUCCESS', 'timestamp': 1514183558296,
                                            'url': 'http://192.168.4.241/jenkins/job/test/36/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#35', 'duration': 154163,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #35', 'id': '35',
                                                                           'keepLog': False, 'number': 35,
                                                                           'queueId': 36, 'result': 'SUCCESS',
                                                                           'timestamp': 1514183403525,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/35/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#34', 'duration': 140753, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #34', 'id': '34', 'keepLog': False, 'number': 34, 'queueId': 35,
             'result': 'SUCCESS', 'timestamp': 1514183245612, 'url': 'http://192.168.4.241/jenkins/job/test/34/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#33',
                                            'duration': 131540, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #33', 'id': '33', 'keepLog': False, 'number': 33,
                                            'queueId': 34, 'result': 'SUCCESS', 'timestamp': 1514182867146,
                                            'url': 'http://192.168.4.241/jenkins/job/test/33/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#32', 'duration': 155124,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #32', 'id': '32',
                                                                           'keepLog': False, 'number': 32,
                                                                           'queueId': 33, 'result': 'SUCCESS',
                                                                           'timestamp': 1514182619834,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/32/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#31', 'duration': 152062, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #31', 'id': '31', 'keepLog': False, 'number': 31, 'queueId': 32,
             'result': 'SUCCESS', 'timestamp': 1514182105926, 'url': 'http://192.168.4.241/jenkins/job/test/31/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#30',
                                            'duration': 132485, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #30', 'id': '30', 'keepLog': False, 'number': 30,
                                            'queueId': 31, 'result': 'SUCCESS', 'timestamp': 1514173196310,
                                            'url': 'http://192.168.4.241/jenkins/job/test/30/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#29', 'duration': 131800,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #29', 'id': '29',
                                                                           'keepLog': False, 'number': 29,
                                                                           'queueId': 30, 'result': 'SUCCESS',
                                                                           'timestamp': 1514172680875,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/29/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#28', 'duration': 141266, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #28', 'id': '28', 'keepLog': False, 'number': 28, 'queueId': 29,
             'result': 'SUCCESS', 'timestamp': 1514171517256, 'url': 'http://192.168.4.241/jenkins/job/test/28/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#27',
                                            'duration': 157847, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #27', 'id': '27', 'keepLog': False, 'number': 27,
                                            'queueId': 27, 'result': 'SUCCESS', 'timestamp': 1514170779424,
                                            'url': 'http://192.168.4.241/jenkins/job/test/27/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#26', 'duration': 163401,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #26', 'id': '26',
                                                                           'keepLog': False, 'number': 26,
                                                                           'queueId': 26, 'result': 'SUCCESS',
                                                                           'timestamp': 1514170560690,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/26/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#25', 'duration': 168759, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #25', 'id': '25', 'keepLog': False, 'number': 25, 'queueId': 25,
             'result': 'SUCCESS', 'timestamp': 1513910829267, 'url': 'http://192.168.4.241/jenkins/job/test/25/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#24',
                                            'duration': 171560, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #24', 'id': '24', 'keepLog': False, 'number': 24,
                                            'queueId': 24, 'result': 'SUCCESS', 'timestamp': 1513910657443,
                                            'url': 'http://192.168.4.241/jenkins/job/test/24/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#23', 'duration': 132006,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #23', 'id': '23',
                                                                           'keepLog': False, 'number': 23,
                                                                           'queueId': 23, 'result': 'SUCCESS',
                                                                           'timestamp': 1513834104180,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/23/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#22', 'duration': 143336, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #22', 'id': '22', 'keepLog': False, 'number': 22, 'queueId': 22,
             'result': 'SUCCESS', 'timestamp': 1513833891685, 'url': 'http://192.168.4.241/jenkins/job/test/22/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [
                {'_class': 'hudson.scm.SubversionChangeLogSet$LogEntry',
                 'affectedPaths': ['src/main/webapp/static/js/process/add_user.js'],
                 'author': {'absoluteUrl': 'http://192.168.4.241/jenkins/user/shengshouze', 'fullName': 'shengshouze'},
                 'commitId': '31295', 'timestamp': 1513756320803, 'date': '2017-12-20T07:52:00.803492Z', 'msg': '',
                 'paths': [{'editType': 'edit',
                            'file': '/code/trunk/java/detao-oa/src/main/webapp/static/js/process/add_user.js'}],
                 'revision': 31295, 'user': 'shengshouze'}, {'_class': 'hudson.scm.SubversionChangeLogSet$LogEntry',
                                                             'affectedPaths': [
                                                                 'src/main/webapp/pages/process/dredge.html'],
                                                             'author': {
                                                                 'absoluteUrl': 'http://192.168.4.241/jenkins/user/shengshouze',
                                                                 'fullName': 'shengshouze'}, 'commitId': '31294',
                                                             'timestamp': 1513756307857,
                                                             'date': '2017-12-20T07:51:47.857402Z', 'msg': '',
                                                             'paths': [{'editType': 'edit',
                                                                        'file': '/code/trunk/java/detao-oa/src/main/webapp/pages/process/dredge.html'}],
                                                             'revision': 31294, 'user': 'shengshouze'},
                {'_class': 'hudson.scm.SubversionChangeLogSet$LogEntry',
                 'affectedPaths': ['src/main/java/cn/detao/oa/service/RatifyService.java',
                                   'src/main/java/cn/detao/oa/service/impl/RatifyServiceImpl.java'],
                 'author': {'absoluteUrl': 'http://192.168.4.241/jenkins/user/shengshouze', 'fullName': 'shengshouze'},
                 'commitId': '31293', 'timestamp': 1513756300436, 'date': '2017-12-20T07:51:40.436261Z', 'msg': '',
                 'paths': [{'editType': 'edit',
                            'file': '/code/trunk/java/detao-oa/src/main/java/cn/detao/oa/service/RatifyService.java'},
                           {'editType': 'edit',
                            'file': '/code/trunk/java/detao-oa/src/main/java/cn/detao/oa/service/impl/RatifyServiceImpl.java'}],
                 'revision': 31293, 'user': 'shengshouze'}, {'_class': 'hudson.scm.SubversionChangeLogSet$LogEntry',
                                                             'affectedPaths': [
                                                                 'src/main/java/cn/detao/oa/controller/PersonnelManagementController.java'],
                                                             'author': {
                                                                 'absoluteUrl': 'http://192.168.4.241/jenkins/user/shengshouze',
                                                                 'fullName': 'shengshouze'}, 'commitId': '31292',
                                                             'timestamp': 1513756294791,
                                                             'date': '2017-12-20T07:51:34.791892Z', 'msg': '',
                                                             'paths': [{'editType': 'edit',
                                                                        'file': '/code/trunk/java/detao-oa/src/main/java/cn/detao/oa/controller/PersonnelManagementController.java'}],
                                                             'revision': 31292, 'user': 'shengshouze'}], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]},
             'culprits': [{'absoluteUrl': 'http://192.168.4.241/jenkins/user/shengshouze', 'fullName': 'shengshouze'}],
             'mavenArtifacts': {}, 'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                  'actions': [{'_class': 'hudson.model.CauseAction',
                                                                               'causes': [{
                                                                                   '_class': 'hudson.model.Cause$UserIdCause',
                                                                                   'shortDescription': 'Started by user sai',
                                                                                   'userId': 'fan',
                                                                                   'userName': 'sai'}]}, {
                                                                                  '_class': 'hudson.scm.SubversionTagAction'},
                                                                              {}, {
                                                                                  '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                              {}, {}, {}], 'artifacts': [],
                                                                  'building': False, 'description': None,
                                                                  'displayName': '#21', 'duration': 75146,
                                                                  'estimatedDuration': 134177, 'executor': None,
                                                                  'fullDisplayName': 'test #21', 'id': '21',
                                                                  'keepLog': False, 'number': 21, 'queueId': 21,
                                                                  'result': 'FAILURE', 'timestamp': 1513693428706,
                                                                  'url': 'http://192.168.4.241/jenkins/job/test/21/',
                                                                  'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                  'culprits': [], 'mavenArtifacts': {},
                                                                  'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#20', 'duration': 75049, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #20', 'id': '20', 'keepLog': False, 'number': 20, 'queueId': 20,
             'result': 'FAILURE', 'timestamp': 1513692309243, 'url': 'http://192.168.4.241/jenkins/job/test/20/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#19',
                                            'duration': 43334, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #19', 'id': '19', 'keepLog': False, 'number': 19,
                                            'queueId': 19, 'result': 'FAILURE', 'timestamp': 1513692207563,
                                            'url': 'http://192.168.4.241/jenkins/job/test/19/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {
                                                                                   '_class': 'jenkins.model.InterruptedBuildAction'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#18', 'duration': 440317,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #18', 'id': '18',
                                                                           'keepLog': False, 'number': 18,
                                                                           'queueId': 18, 'result': 'ABORTED',
                                                                           'timestamp': 1513690597493,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/18/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#17', 'duration': 52946, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #17', 'id': '17', 'keepLog': False, 'number': 17, 'queueId': 17,
             'result': 'SUCCESS', 'timestamp': 1513688552170, 'url': 'http://192.168.4.241/jenkins/job/test/17/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#16',
                                            'duration': 34393, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #16', 'id': '16', 'keepLog': False, 'number': 16,
                                            'queueId': 16, 'result': 'SUCCESS', 'timestamp': 1513688180711,
                                            'url': 'http://192.168.4.241/jenkins/job/test/16/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#15', 'duration': 28108,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #15', 'id': '15',
                                                                           'keepLog': False, 'number': 15,
                                                                           'queueId': 15, 'result': 'FAILURE',
                                                                           'timestamp': 1513688027833,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/15/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#14', 'duration': 23852, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #14', 'id': '14', 'keepLog': False, 'number': 14, 'queueId': 14,
             'result': 'SUCCESS', 'timestamp': 1513675851908, 'url': 'http://192.168.4.241/jenkins/job/test/14/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#13',
                                            'duration': 23299, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #13', 'id': '13', 'keepLog': False, 'number': 13,
                                            'queueId': 13, 'result': 'SUCCESS', 'timestamp': 1513675755391,
                                            'url': 'http://192.168.4.241/jenkins/job/test/13/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#12', 'duration': 23360,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #12', 'id': '12',
                                                                           'keepLog': False, 'number': 12,
                                                                           'queueId': 12, 'result': 'SUCCESS',
                                                                           'timestamp': 1513675687558,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/12/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#11', 'duration': 25238, 'estimatedDuration': 134177,
             'executor': None, 'fullDisplayName': 'test #11', 'id': '11', 'keepLog': False, 'number': 11, 'queueId': 11,
             'result': 'FAILURE', 'timestamp': 1513675645642, 'url': 'http://192.168.4.241/jenkins/job/test/11/',
             'builtOn': '', 'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
             'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
                {'_class': 'hudson.model.CauseAction', 'causes': [
                    {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai',
                     'userId': 'fan', 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
                {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                            'building': False, 'description': None, 'displayName': '#10',
                                            'duration': 24968, 'estimatedDuration': 134177, 'executor': None,
                                            'fullDisplayName': 'test #10', 'id': '10', 'keepLog': False, 'number': 10,
                                            'queueId': 10, 'result': 'FAILURE', 'timestamp': 1513675514011,
                                            'url': 'http://192.168.4.241/jenkins/job/test/10/', 'builtOn': '',
                                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                          'kind': 'svn', 'revisions': [
                                                    {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                     'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
                                            'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#9', 'duration': 31889,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #9', 'id': '9',
                                                                           'keepLog': False, 'number': 9, 'queueId': 9,
                                                                           'result': 'FAILURE',
                                                                           'timestamp': 1513675422192,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/9/',
                                                                           'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#8', 'duration': 23377, 'estimatedDuration': 134177, 'executor': None,
             'fullDisplayName': 'test #8', 'id': '8', 'keepLog': False, 'number': 8, 'queueId': 8, 'result': 'FAILURE',
             'timestamp': 1513675369582, 'url': 'http://192.168.4.241/jenkins/job/test/8/', 'builtOn': '',
             'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn', 'revisions': [
                 {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]}, 'culprits': [],
             'mavenArtifacts': {}, 'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                  'actions': [{'_class': 'hudson.model.CauseAction',
                                                                               'causes': [{
                                                                                   '_class': 'hudson.model.Cause$UserIdCause',
                                                                                   'shortDescription': 'Started by user sai',
                                                                                   'userId': 'fan',
                                                                                   'userName': 'sai'}]}, {
                                                                                  '_class': 'hudson.scm.SubversionTagAction'},
                                                                              {}, {
                                                                                  '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                              {}, {}, {}], 'artifacts': [],
                                                                  'building': False, 'description': None,
                                                                  'displayName': '#7', 'duration': 23028,
                                                                  'estimatedDuration': 134177, 'executor': None,
                                                                  'fullDisplayName': 'test #7', 'id': '7',
                                                                  'keepLog': False, 'number': 7, 'queueId': 7,
                                                                  'result': 'SUCCESS', 'timestamp': 1513675281472,
                                                                  'url': 'http://192.168.4.241/jenkins/job/test/7/',
                                                                  'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                  'culprits': [], 'mavenArtifacts': {},
                                                                  'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#6', 'duration': 25299, 'estimatedDuration': 134177, 'executor': None,
             'fullDisplayName': 'test #6', 'id': '6', 'keepLog': False, 'number': 6, 'queueId': 6, 'result': 'SUCCESS',
             'timestamp': 1513675241777, 'url': 'http://192.168.4.241/jenkins/job/test/6/', 'builtOn': '',
             'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn', 'revisions': [
                 {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]}, 'culprits': [],
             'mavenArtifacts': {}, 'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                  'actions': [{'_class': 'hudson.model.CauseAction',
                                                                               'causes': [{
                                                                                   '_class': 'hudson.model.Cause$UserIdCause',
                                                                                   'shortDescription': 'Started by user sai',
                                                                                   'userId': 'fan',
                                                                                   'userName': 'sai'}]}, {
                                                                                  '_class': 'hudson.scm.SubversionTagAction'},
                                                                              {}, {
                                                                                  '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                              {}, {}, {}], 'artifacts': [],
                                                                  'building': False, 'description': None,
                                                                  'displayName': '#5', 'duration': 24378,
                                                                  'estimatedDuration': 134177, 'executor': None,
                                                                  'fullDisplayName': 'test #5', 'id': '5',
                                                                  'keepLog': False, 'number': 5, 'queueId': 5,
                                                                  'result': 'FAILURE', 'timestamp': 1513675140915,
                                                                  'url': 'http://192.168.4.241/jenkins/job/test/5/',
                                                                  'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                  'culprits': [], 'mavenArtifacts': {},
                                                                  'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#4', 'duration': 25148, 'estimatedDuration': 134177, 'executor': None,
             'fullDisplayName': 'test #4', 'id': '4', 'keepLog': False, 'number': 4, 'queueId': 4, 'result': 'FAILURE',
             'timestamp': 1513675066853, 'url': 'http://192.168.4.241/jenkins/job/test/4/', 'builtOn': '',
             'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn', 'revisions': [
                 {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]}, 'culprits': [],
             'mavenArtifacts': {}, 'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                  'actions': [{'_class': 'hudson.model.CauseAction',
                                                                               'causes': [{
                                                                                   '_class': 'hudson.model.Cause$UserIdCause',
                                                                                   'shortDescription': 'Started by user sai',
                                                                                   'userId': 'fan',
                                                                                   'userName': 'sai'}]}, {
                                                                                  '_class': 'hudson.scm.SubversionTagAction'},
                                                                              {}, {
                                                                                  '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                              {}, {}, {}], 'artifacts': [],
                                                                  'building': False, 'description': None,
                                                                  'displayName': '#3', 'duration': 24653,
                                                                  'estimatedDuration': 134177, 'executor': None,
                                                                  'fullDisplayName': 'test #3', 'id': '3',
                                                                  'keepLog': False, 'number': 3, 'queueId': 3,
                                                                  'result': 'FAILURE', 'timestamp': 1513674974187,
                                                                  'url': 'http://192.168.4.241/jenkins/job/test/3/',
                                                                  'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                  'culprits': [], 'mavenArtifacts': {},
                                                                  'mavenVersionUsed': '3.5.2'},
            {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                        'causes': [
                                                                            {'_class': 'hudson.model.Cause$UserIdCause',
                                                                             'shortDescription': 'Started by user sai',
                                                                             'userId': 'fan', 'userName': 'sai'}]},
                                                                       {'_class': 'hudson.scm.SubversionTagAction'}, {},
                                                                       {
                                                                           '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                       {}, {}, {}], 'artifacts': [], 'building': False,
             'description': None, 'displayName': '#2', 'duration': 30866, 'estimatedDuration': 134177, 'executor': None,
             'fullDisplayName': 'test #2', 'id': '2', 'keepLog': False, 'number': 2, 'queueId': 2, 'result': 'FAILURE',
             'timestamp': 1513674734883, 'url': 'http://192.168.4.241/jenkins/job/test/2/', 'builtOn': '',
             'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn', 'revisions': [
                 {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]}, 'culprits': [],
             'mavenArtifacts': {}, 'mavenVersionUsed': '3.5.2'}, {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                  'actions': [{'_class': 'hudson.model.CauseAction',
                                                                               'causes': [{
                                                                                   '_class': 'hudson.model.Cause$UserIdCause',
                                                                                   'shortDescription': 'Started by user sai',
                                                                                   'userId': 'fan',
                                                                                   'userName': 'sai'}]}, {
                                                                                  '_class': 'hudson.scm.SubversionTagAction'},
                                                                              {}, {
                                                                                  '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                              {}, {}, {}], 'artifacts': [],
                                                                  'building': False, 'description': None,
                                                                  'displayName': '#1', 'duration': 346337,
                                                                  'estimatedDuration': 134177, 'executor': None,
                                                                  'fullDisplayName': 'test #1', 'id': '1',
                                                                  'keepLog': False, 'number': 1, 'queueId': 1,
                                                                  'result': 'SUCCESS', 'timestamp': 1513673818043,
                                                                  'url': 'http://192.168.4.241/jenkins/job/test/1/',
                                                                  'builtOn': '', 'changeSet': {
                    '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31157}]},
                                                                  'culprits': [], 'mavenArtifacts': {},
                                                                  'mavenVersionUsed': '3.5.2'}], 'color': 'blue',
        'firstBuild': {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                                  'causes': [{
                                                                                      '_class': 'hudson.model.Cause$UserIdCause',
                                                                                      'shortDescription': 'Started by user sai',
                                                                                      'userId': 'fan',
                                                                                      'userName': 'sai'}]}, {
                                                                                     '_class': 'hudson.scm.SubversionTagAction'},
                                                                                 {}, {
                                                                                     '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                                 {}, {}, {}], 'artifacts': [],
                       'building': False, 'description': None, 'displayName': '#1', 'duration': 346337,
                       'estimatedDuration': 134177, 'executor': None, 'fullDisplayName': 'test #1', 'id': '1',
                       'keepLog': False, 'number': 1, 'queueId': 1, 'result': 'SUCCESS', 'timestamp': 1513673818043,
                       'url': 'http://192.168.4.241/jenkins/job/test/1/', 'builtOn': '',
                       'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                     'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                    'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
                       'mavenVersionUsed': '3.5.2'}, 'healthReport': [
        {'description': 'Build stability: No recent builds failed.', 'iconClassName': 'icon-health-80plus',
         'iconUrl': 'health-80plus.png', 'score': 100}], 'inQueue': False, 'keepDependencies': False,
        'lastBuild': {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [{'_class': 'hudson.model.CauseAction',
                                                                                 'causes': [{
                                                                                     '_class': 'hudson.model.Cause$UserIdCause',
                                                                                     'shortDescription': 'Started by user sai',
                                                                                     'userId': 'fan',
                                                                                     'userName': 'sai'}]}, {
                                                                                    '_class': 'hudson.scm.SubversionTagAction'},
                                                                                {}, {
                                                                                    '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                                {}, {}, {}], 'artifacts': [],
                      'building': False, 'description': None, 'displayName': '#46', 'duration': 147382,
                      'estimatedDuration': 134177, 'executor': None, 'fullDisplayName': 'test #46', 'id': '46',
                      'keepLog': False, 'number': 46, 'queueId': 47, 'result': 'SUCCESS', 'timestamp': 1514342734339,
                      'url': 'http://192.168.4.241/jenkins/job/test/46/', 'builtOn': '',
                      'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                    'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                   'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                      'mavenVersionUsed': '3.5.2'}, 'lastCompletedBuild': {'_class': 'hudson.maven.MavenModuleSetBuild',
                                                                           'actions': [
                                                                               {'_class': 'hudson.model.CauseAction',
                                                                                'causes': [{
                                                                                    '_class': 'hudson.model.Cause$UserIdCause',
                                                                                    'shortDescription': 'Started by user sai',
                                                                                    'userId': 'fan',
                                                                                    'userName': 'sai'}]}, {
                                                                                   '_class': 'hudson.scm.SubversionTagAction'},
                                                                               {}, {
                                                                                   '_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
                                                                               {}, {}, {}], 'artifacts': [],
                                                                           'building': False, 'description': None,
                                                                           'displayName': '#46', 'duration': 147382,
                                                                           'estimatedDuration': 134177,
                                                                           'executor': None,
                                                                           'fullDisplayName': 'test #46', 'id': '46',
                                                                           'keepLog': False, 'number': 46,
                                                                           'queueId': 47, 'result': 'SUCCESS',
                                                                           'timestamp': 1514342734339,
                                                                           'url': 'http://192.168.4.241/jenkins/job/test/46/',
                                                                           'builtOn': '', 'changeSet': {
            '_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
            'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa', 'revision': 31295}]},
                                                                           'culprits': [], 'mavenArtifacts': {},
                                                                           'mavenVersionUsed': '3.5.2'},
        'lastFailedBuild': {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
            {'_class': 'hudson.model.CauseAction', 'causes': [
                {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai', 'userId': 'fan',
                 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
            {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                            'building': False, 'description': None, 'displayName': '#21', 'duration': 75146,
                            'estimatedDuration': 134177, 'executor': None, 'fullDisplayName': 'test #21', 'id': '21',
                            'keepLog': False, 'number': 21, 'queueId': 21, 'result': 'FAILURE',
                            'timestamp': 1513693428706, 'url': 'http://192.168.4.241/jenkins/job/test/21/',
                            'builtOn': '',
                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31157}]}, 'culprits': [], 'mavenArtifacts': {},
                            'mavenVersionUsed': '3.5.2'},
        'lastStableBuild': {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
            {'_class': 'hudson.model.CauseAction', 'causes': [
                {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai', 'userId': 'fan',
                 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
            {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                            'building': False, 'description': None, 'displayName': '#46', 'duration': 147382,
                            'estimatedDuration': 134177, 'executor': None, 'fullDisplayName': 'test #46', 'id': '46',
                            'keepLog': False, 'number': 46, 'queueId': 47, 'result': 'SUCCESS',
                            'timestamp': 1514342734339, 'url': 'http://192.168.4.241/jenkins/job/test/46/',
                            'builtOn': '',
                            'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                          'revisions': [{'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                         'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                            'mavenVersionUsed': '3.5.2'},
        'lastSuccessfulBuild': {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
            {'_class': 'hudson.model.CauseAction', 'causes': [
                {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user sai', 'userId': 'fan',
                 'userName': 'sai'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
            {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'}, {}, {}, {}], 'artifacts': [],
                                'building': False, 'description': None, 'displayName': '#46', 'duration': 147382,
                                'estimatedDuration': 134177, 'executor': None, 'fullDisplayName': 'test #46',
                                'id': '46', 'keepLog': False, 'number': 46, 'queueId': 47, 'result': 'SUCCESS',
                                'timestamp': 1514342734339, 'url': 'http://192.168.4.241/jenkins/job/test/46/',
                                'builtOn': '',
                                'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [], 'kind': 'svn',
                                              'revisions': [
                                                  {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                                   'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                'mavenVersionUsed': '3.5.2'}, 'lastUnstableBuild': None,
        'lastUnsuccessfulBuild': {'_class': 'hudson.maven.MavenModuleSetBuild', 'actions': [
            {'_class': 'hudson.model.CauseAction', 'causes': [
                {'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user admin',
                 'userId': 'admin', 'userName': 'admin'}]}, {'_class': 'hudson.scm.SubversionTagAction'}, {},
            {'_class': 'hudson.maven.reporters.MavenAggregatedArtifactRecord'},
            {'_class': 'jenkins.model.InterruptedBuildAction'}, {}, {}, {}], 'artifacts': [], 'building': False,
                                  'description': None, 'displayName': '#41', 'duration': 93570,
                                  'estimatedDuration': 134177, 'executor': None, 'fullDisplayName': 'test #41',
                                  'id': '41', 'keepLog': False, 'number': 41, 'queueId': 42, 'result': 'ABORTED',
                                  'timestamp': 1514297227747, 'url': 'http://192.168.4.241/jenkins/job/test/41/',
                                  'builtOn': '',
                                  'changeSet': {'_class': 'hudson.scm.SubversionChangeLogSet', 'items': [],
                                                'kind': 'svn', 'revisions': [
                                          {'module': 'svn://192.168.4.15:3691/code/trunk/java/detao-oa',
                                           'revision': 31295}]}, 'culprits': [], 'mavenArtifacts': {},
                                  'mavenVersionUsed': '3.5.2'}, 'nextBuildNumber': 47,
        'property': [{'_class': 'com.tikal.hudson.plugins.notification.HudsonNotificationProperty'}], 'queueItem': None,
        'concurrentBuild': False, 'downstreamProjects': [],
        'scm': {'_class': 'hudson.scm.SubversionSCM', 'type': 'hudson.scm.SubversionSCM', 'browser': None,
                'excludedCommitMessages': '', 'excludedRegions': '', 'excludedRevprop': '', 'excludedUsers': '',
                'filterChangelog': False, 'ignoreDirPropChanges': False, 'includedRegions': '', 'locations': [{}],
                'quietOperation': True, 'workspaceUpdater': {'_class': 'hudson.scm.subversion.UpdateUpdater'}},
        'upstreamProjects': [], 'modules': [
        {'actions': [{}, {}], 'description': None, 'displayNameOrNull': None, 'fullDisplayName': 'test » detao-oa',
         'fullName': 'test/detao-oa:detao-oa', 'name': 'detao-oa:detao-oa',
         'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/', 'buildable': True, 'builds': [
            {'_class': 'hudson.maven.MavenBuild', 'number': 46,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/46/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 45,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/45/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 44,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/44/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 43,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/43/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 42,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/42/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 41,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/41/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 40,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/40/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 39,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/39/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 38,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/38/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 37,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/37/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 36,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/36/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 35,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/35/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 34,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/34/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 33,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/33/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 32,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/32/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 31,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/31/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 30,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/30/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 29,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/29/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 28,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/28/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 27,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/27/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 26,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/26/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 25,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/25/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 24,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/24/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 23,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/23/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 22,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/22/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 21,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/21/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 20,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/20/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 19,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/19/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 18,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/18/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 17,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/17/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 16,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/16/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 15,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/15/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 14,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/14/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 13,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/13/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 12,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/12/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 11,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/11/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 10,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/10/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 9,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/9/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 8,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/8/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 7,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/7/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 6,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/6/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 5,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/5/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 4,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/4/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 3,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/3/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 2,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/2/'},
            {'_class': 'hudson.maven.MavenBuild', 'number': 1,
             'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/1/'}], 'color': 'blue',
         'firstBuild': {'_class': 'hudson.maven.MavenBuild', 'number': 1,
                        'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/1/'}, 'healthReport': [
            {'description': 'Build stability: No recent builds failed.', 'iconClassName': 'icon-health-80plus',
             'iconUrl': 'health-80plus.png', 'score': 100}], 'inQueue': False, 'keepDependencies': False,
         'lastBuild': {'_class': 'hudson.maven.MavenBuild', 'number': 46,
                       'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/46/'},
         'lastCompletedBuild': {'_class': 'hudson.maven.MavenBuild', 'number': 46,
                                'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/46/'},
         'lastFailedBuild': None, 'lastStableBuild': {'_class': 'hudson.maven.MavenBuild', 'number': 46,
                                                      'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/46/'},
         'lastSuccessfulBuild': {'_class': 'hudson.maven.MavenBuild', 'number': 46,
                                 'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/46/'},
         'lastUnstableBuild': None, 'lastUnsuccessfulBuild': {'_class': 'hudson.maven.MavenBuild', 'number': 39,
                                                              'url': 'http://192.168.4.241/jenkins/job/test/detao-oa$detao-oa/39/'},
         'nextBuildNumber': 47, 'property': [], 'queueItem': None, 'concurrentBuild': False, 'downstreamProjects': [],
         'scm': {'_class': 'hudson.scm.NullSCM'}, 'upstreamProjects': [], 'displayName': 'detao-oa'}]}
