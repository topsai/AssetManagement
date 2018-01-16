#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import docker
from django.conf import settings

client = docker.DockerClient(base_url=settings.DOCKER_SERVER, version='1.29')
