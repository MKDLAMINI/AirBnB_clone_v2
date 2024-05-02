#!/usr/bin/python3
"""
Fabric script for deploying a web_static archive to web servers
"""

from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['34.207.211.211', '54.161.236.197']

def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive
    and stores it in the versions directory
    Returns:
        Path to the created archive if successful, None otherwise
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    local("mkdir -p versions")
    create_archive = local(f"tar -cvzf versions/{archive_name} web_static")
    if create_archive is not None:
        return f"versions/{archive_name}"
    else:
        return None

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

def deploy():
    """
    Creates and distributes an archive to web servers using deploy
    """
    # Call do_pack and store the path of the created archive
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
