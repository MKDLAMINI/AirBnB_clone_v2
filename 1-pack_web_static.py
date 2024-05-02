#!/usr/bin/python3
"""
Fabric script to genereate tgz archive with do_pack
"""

from fabric.api import *
from datetime import datetime


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
