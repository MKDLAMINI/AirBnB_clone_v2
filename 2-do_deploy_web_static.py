#!/usr/bin/python3
"""
Fabric script for deploying a web_static archive to web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['34.207.211.211', '54.161.236.197']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers

    Args:
        archive_path (str): Path to the archive file to deploy

    Returns:
        bool: True if deployment is successful, False otherwise
    """
    try:
        # Check if the archive exists locally
        if not exists(archive_path):
            return False

        full_file_name = archive_path.split("/")[-1]
        file_name = full_file_name.split(".")[0]
        base_path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run(f'mkdir -p {base_path}{file_name}/')
        run(f'tar -xzf /tmp/{full_file_name} -C {base_path}{file_name}/')
        run(f'rm /tmp/{full_file_name}')
        run(f'mv {base_path}{file_name}/web_static/* {base_path}{file_name}/')
        run(f'rm -rf {base_path}{file_name}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {base_path}{file_name}/ /data/web_static/current')

        print("New version deployed!")
        return True
    except Exception as e:
        return False
