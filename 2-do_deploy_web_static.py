#!/usr/bin/python3
"""
Fabric script for deploying a web_static archive to web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['34.207.211.211', '54.161.236.197']


def do_deploy(archive_path):
<<<<<<< HEAD
    """
    Distribute an archive to web servers

    Args:
        archive_path (str): Path to the archive file to deploy

    Returns:
        bool: True if deployment is successful, False otherwise
    """
=======
    """distributes an archive to the web servers"""
>>>>>>> c32bdad278dedf018ff48615d73b4fd6fb7b7dc4
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
