#!/usr/bin/python3
""" creates and distributes an archive to your web servers,
using the function deploy with a cleanup function"""


from fabric.api import *
from time import strftime
from datetime import date


env.hosts = ['100.26.255.19', '54.237.2.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """generates tar gz from web-static"""
    file_name = f"web_static_{strftime('%Y%m%d%H%M%S')}.tgz"
    try:
        local("mkdir -p versions")
        res = local(f"tar -czvf versions/{file_name} web_static/")

        return f"versions/{file_name}" if res.succeeded else None

    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    from os import path

    if not archive_path:
        return False

    name_with_no_ext = archive_path.split('.')[0].split("/")[1]
    try:
        if not path.exists(archive_path):
            return False
        put(local_path=archive_path, remote_path="/tmp/")
        run(f"mkdir -p /data/web_static/releases/{name_with_no_ext}")
        run(f"tar -xzf /tmp/{name_with_no_ext}.tgz -C \
 /data/web_static/releases/{name_with_no_ext}/")
        run(f"rm /tmp/{name_with_no_ext}.tgz")
        run(f"mv /data/web_static/releases/{name_with_no_ext}/web_static/*\
 /data/web_static/releases/{name_with_no_ext}/")
        run(f"rm -rf /data/web_static/releases/{name_with_no_ext}/web_static")
        run(f"unlink /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{name_with_no_ext}\
 /data/web_static/current")
        return True
    except Exception as e:
        return False


def deploy():
    """deploys to the servers"""
    pack_path = do_pack()
    return do_deploy(pack_path)


def do_clean(number=0):
    """removes outdated versions"""
    from os import listdir
    number = 1 if int(number) == 0 else int(number)

    versions = sorted(listdir("versions"))
    [versions.pop() for i in range(number)]
    with lcd("versions"):
        [local(f"rm ./{_}") for _ in versions]

    with cd("/data/web_static/releases"):
        versions = run("ls -tr").split()
        versions = [a for a in versions if "web_static_" in a]
        [versions.pop() for i in range(number)]
        [run(f"rm -rf ./{_}") for _ in versions]
