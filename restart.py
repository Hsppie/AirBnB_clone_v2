#!/usr/bin/python3
from fabric.api import *

env.hosts = ['52.91.119.110','52.91.151.232']
env.user = 'ubuntu'
@task
def restart():
    run('sudo systemctl restart nginx')

