#!/usr/bin/python3
# module with method that cleans specified number of archives

from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['35.231.100.106', '35.237.151.115']


def do_clean(number=0):
    """ deletes out of date archives """
    number = int(number)
    with lcd('versions'):
        if number == 0 or number == 1:
            local('ls -tr | head -n -1 | xargs rm -rfv')
        else:
            local('ls -tr | head -n -{} | xargs rm -rfv'.format(number))
    with cd('/data/web_static/releases'):
        if number == 0 or number == 1:
            run('ls -tr | head -n - 1 | xargs rm -rfv')
        else:
            run('ls -tr | head -n -{} | xargs rm -rfv'.format(number))
