#!/usr/bin/python3
"""generates tar gz from web-static"""


from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """generates tar gz from web-static"""
    file_name = f"web_static_{strftime('%Y%m%d%H%M%S')}.tgz"
    try:
        local("mkdir -p versions")
        res = local(f"tar -czvf versions/{file_name} web_static/")

        return f"versions/{file_name}" if res.succeeded else None

    except Exception as e:
        return None
