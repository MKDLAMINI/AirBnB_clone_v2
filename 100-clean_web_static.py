#!/usr/bin/python3
"""
Fabric script for cleaning up old archives and deployments
"""

from fabric.api import *
import os

env.hosts = ['34.207.211.211', '54.161.236.197']


def do_clean(number=0):
    """
    Deletes out-of-date archives and deployments

    Args:
        number (int): Number of archives to keep

    Returns:
        None
    """
    number = max(int(number), 1)

    with lcd("versions"):
        local_arch = sorted(os.listdir("."))
        to_delete_local = (local_arch[:-number] if number < len(local_arch)
                           else [])
        [local("rm -f ./{}".format(arc)) for arc in to_delete_local]

    with cd("/data/web_static/releases"):
        remote_arch = run("ls -tr").split()
        remote_arch = [arc for arc in remote_arch if "web_static_" in arc]
        to_delete_remote = (remote_arch[:-number] if number < len(remote_arch)
                            else [])
        [run("rm -rf ./{}".format(arc)) for arc in to_delete_remote]
