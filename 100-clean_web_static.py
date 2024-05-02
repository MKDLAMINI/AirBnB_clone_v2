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
    number = 1 if int(number) == 0 else int(number)

    all_arcs = sorted(os.listdir("versions"))
    [all_arcs.pop() for index in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(arc)) for arc in all_arcs]

    with cd("/data/web_static/releases"):
        all_arcs = run("ls -tr").split()
        all_arcs = [arc for arc in all_arcs if "web_static_" in arc]
        [all_arcs.pop() for index in range(number)]
        [run("rm -rf ./{}".format(arc)) for arc in all_arcs]
