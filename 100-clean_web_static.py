#!/usr/bin/python3
""" Function deploys webstatic archive to web servers"""
from fabric.api import *


env.hosts = ['', '']
env.user = "ubuntu"


def do_clean(number=0):
    """ method cleans up after deployment"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
