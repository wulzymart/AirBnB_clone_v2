#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""


from fabric.api import *
from os import path

env.hosts = ['100.26.255.19', '54.237.2.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not archive_path or not path.exists(archive_path)\
            or not path.isfile(archive_path):
        return False

    name_with_no_ext = path.basename(archive_path).split('.')[0]

    if put(local_path=archive_path, remote_path="/tmp/").failed or\
        run(f"mkdir -p /data/web_static/releases/{\
            name_with_no_ext}").failed or\
        run(f"tar -xzf /tmp/{name_with_no_ext}.tgz -C \
 /data/web_static/releases/{name_with_no_ext}/").failed or\
        run(f"rm /tmp/{name_with_no_ext}.tgz").failed or\
        run(f"mv /data/web_static/releases/{name_with_no_ext}/web_static/*\
 /data/web_static/releases/{name_with_no_ext}/").failed or\
        run(f"rm -rf /data/web_static/releases/{\
            name_with_no_ext}/web_static").failed or\
        run(f"rm -rf /data/web_static/current").failed or\
        run(f"ln -s /data/web_static/releases/{name_with_no_ext}\
 /data/web_static/current").failed:
        return False
    return True
