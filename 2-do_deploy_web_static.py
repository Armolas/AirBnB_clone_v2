#!/usr/bin/python3
"""distributes an archive to web servers, using the function do_deploy"""
from fabric.api import *
from datetime import datetime
import os
import re


env.hosts = [
    '54.227.121.152',
    '34.203.75.120'
]
env.user = 'ubuntu'
def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_name = f"web_static_{time}.tgz"
    local('mkdir -p versions')
    result = local(f'tar -cvzf versions/{tar_name} web_static')
    if result.succeeded:
        return f"/versions/{tar_name}"
    else:
        return None

def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    filename = re.compile(r'web_static_\d+')
    match = filename.search(archive_path)
    filename = match.group()
    put(local_path=archive_path, remote_path='/tmp/')
    run(f'mkdir -p /data/web_static/releases/{filename}')
    run(f'tar -xzf /tmp/{filename}.tgz -C /data/web_static/releases/{filename}')
    run(f'rm /tmp/{filename}.tgz')
    run(f'mv /data/web_static/releases/{filename}/web_static/* /data/web_static/releases/{filename}/')
    run(f'rm -rf /data/web_static/releases/{filename}/web_static')
    run(f'rm -rf /data/web_static/current')
    result = run(f'ln -s /data/web_static/releases/{filename} /data/web_static/current')
    if result.succeeded:
        return True
    else:
        return False
