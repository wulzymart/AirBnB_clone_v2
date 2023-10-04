#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""


from fabric.api import *
import os

env.hosts = ['100.26.255.19', '54.237.2.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


# def do_deploy(archive_path):
#     """distributes an archive to your web servers"""

#     if not archive_path or not path.exists(archive_path)\
#             or not path.isfile(archive_path):
#         return False

#     name_with_no_ext = path.basename(archive_path).split('.')[0]

#     if put(local_path=archive_path, remote_path="/tmp/").failed or\
#         run(f"mkdir -p /data/web_static/releases/{\
#             name_with_no_ext}").failed or\
#         run(f"tar -xzf /tmp/{name_with_no_ext}.tgz -C \
#  /data/web_static/releases/{name_with_no_ext}/").failed or\
#         run(f"rm /tmp/{name_with_no_ext}.tgz").failed or\
#         run(f"mv /data/web_static/releases/{name_with_no_ext}/web_static/*\
#  /data/web_static/releases/{name_with_no_ext}/").failed or\
#         run(f"rm -rf /data/web_static/releases/{\
#             name_with_no_ext}/web_static").failed or\
#         run(f"rm -rf /data/web_static/current").failed or\
#         run(f"ln -s /data/web_static/releases/{name_with_no_ext}\
#  /data/web_static/current").failed:
#         return False
#     return True

def do_deploy(archive_path):
    """Distributes an archive to my web servers.
    Args:
        archive_path (string): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
