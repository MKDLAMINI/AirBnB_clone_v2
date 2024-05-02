#!/usr/bin/python3
"""
Fabric script for cleaning up old archives and deployments
"""

from fabric.api import env, run, local
from fabric.operations import get, put
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
    try:
        number = int(number)
        if number < 1:
            number = 1

        local('ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}'.format(number + 1))

        for host in env.hosts:
            with settings(host_string=host):
                releases = run('ls -t /data/web_static/releases/')
                releases_list = releases.split()
                if len(releases_list) > number:
                    old_releases = ' '.join(releases_list[number:])
                    run('rm -rf /data/web_static/releases/{}'.format(old_releases))
        print("Cleaned old archives successfully.")
    except Exception as e:
        print(f"Error cleaning archives: {e}")
