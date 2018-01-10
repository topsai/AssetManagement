#! /usr/bin/env python
# -*- coding: utf-8 -*-


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
def cut_conf1(file):
    conf_dict = {'global': {}, 'events': {}, 'http': {}}
    conf_key = 'global'

    for i in file.split('\n'):

        # print(conf_key)
        line = i.strip().strip(';')

        # 去除已注释配置
        if line.startswith('#'):
            continue
        print('line:', line)
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


def cut_conf(file):
    conf_dict = {'global': {}, 'events': {}, 'http': {}}
    conf_key = 'global'

    with open(file, 'r') as f:
        for i in f:
            # print(conf_key)
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
