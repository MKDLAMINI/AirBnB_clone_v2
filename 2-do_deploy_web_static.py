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

        archive_name = archive_path.split("/")[-1]
        target_folder = f"/data/web_static/releases/{archive_name.split('.')[0]}"

        put(archive_path, '/tmp/')

        run(f'mkdir -p {target_folder}')
        run(f'tar -xzf /tmp/{archive_name} -C {target_folder}')

        run(f'rm /tmp/{archive_name}')

        run(f'mv {target_folder}/web_static/* {target_folder}/')
        run(f'rm -rf {target_folder}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {target_folder} /data/web_static/current')

        print("New version deployed!")
        return True
    except:
        return False
