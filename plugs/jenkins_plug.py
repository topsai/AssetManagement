#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import jenkins


# 操作jenkins类
class MyJenkins:
    def __init__(self):
        # 定义远程的jenkins master server的url，以及port
        self.jenkins_server_url = 'http://192.168.202.143/jenkins'
        # 定义用户的User Id 和 API Token，获取方式同上文
        self.user_id = 'fan'
        self.api_token = '8c8f1a1841b248fb37a2d55fd516d6a9'
        self.job_name = 'test'
        self.param_dict = ''
        self.build_number = 22
        self.server = None

        # print('check running job...')
        # while True:
        #     time.sleep(0.5)
        #
        #     if len(server.get_running_builds()) == 0:
        #         print('build success')
        #         break
        #     else:
        #         time.sleep(1)
        #
        #         print('{} running build'.format(job_name))
        #         queue_info = server.get_queue_info()
        #         print(queue_info)

        # String参数化构建job名为job_name的job, 参数param_dict为字典形式，如：param_dict= {"param1"：“value1”， “param2”：“value2”}
        # server.build_job(job_name, parameters=param_dict)

        # queue_info = server.get_queue_info()

    def conn(self):
        # 实例化jenkins对象，连接远程的jenkins master server
        self.server = jenkins.Jenkins(self.jenkins_server_url, username=self.user_id, password=self.api_token)

    def build(self, job_name):
        # 构建job名为job_name的job（不带构建参数）
        self.server.build_job(job_name)

    def get_job_info(self, job_name):
        # 获取job名为job_name的job的相关信息
        return self.server.get_job_info(job_name)

    def get_running_builds(self):
        # 获取正在构建的项目
        return self.server.get_running_builds()

    def get_build_info(self, job_name, number):
        # 获取job名为job_name的job的最后次构建号
        return self.server.get_build_info(job_name, number, depth=0)

    def get_buildresult(self, job_name, buildid):
        # 获取job名为job_name的job的某次构建的执行结果状态
        return self.server.get_build_info(job_name, buildid)['result']

    def build_status(self, job_name, buildid):
        # 判断job名为job_name的job的某次构建是否还在构建中
        return self.server.get_build_info(job_name, buildid)['building']

    def getsvnnum(self, job_name, buildid):
        # 获取某次构建的svn提交数
        return self.server.get_build_info(job_name, buildid)['changeSet']['revisions'][0]['revision']
