#!/usr/bin/python3
"""Compress before shipping
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress directory
    Return:
        path to archive on success;
        None on fail
    """
    # Get current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static'.format(archive_path))

    # Check if archiving was successful
    if result.failed:
        return None
    return archive_path
