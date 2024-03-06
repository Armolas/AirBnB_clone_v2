#!/usr/bin/python3
"""uses fabric to generate an archive of web_static folder."""
from fabric.api import local
from datetime import datetime


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
