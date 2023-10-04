#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""


from fabric.api import *
from time import strftime
from datetime import date
from os import path

env.hosts = ['100.26.255.19', '54.237.2.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not archive_path:
        return False

    name_with_no_ext = archive_path.split('.')[0].split("/")[1]
    try:
        if not path.exists(archive_path):
            return False
        put(local_path=archive_path, remote_path="/tmp/")
        run(f"sudo mkdir -p /data/web_static/releases/{name_with_no_ext}")
        run(f"sudo tar -xzf /tmp/{name_with_no_ext}.tgz -C \
 /data/web_static/releases/{name_with_no_ext}/")
        run(f"sudo rm /tmp/{name_with_no_ext}.tgz")
        run(f"sudomv /data/web_static/releases/{name_with_no_ext}/web_static/*\
 /data/web_static/releases/{name_with_no_ext}/")
        run(f"sudo rm -rf /data/web_static/releases/{name_with_no_ext}/web_static")
        run(f"sudo unlink /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{name_with_no_ext}\
 /data/web_static/current")
        return True
    except Exception as e:
        return False
