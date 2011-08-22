from fabric.api import *

@task
def check_uptime():
    ''' Displays server uptime '''
    run('uptime')


@task
def apt_get_dist_upgrade():
    ''' Executes apt-get upgrade && apt-get dist-upgrade '''
    sudo('apt-get upgrade && apt-get dist-upgrade --assume-yes')


@task
def load_average():
    ''' Displays server load avg from /proc/loadavg'''
    run('cat /proc/loadavg')
