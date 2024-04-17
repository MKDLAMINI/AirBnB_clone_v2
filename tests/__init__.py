#!/usr/bin/python3
"""Tests for the AirBnb clone modules.
"""
import os
from models.engine.file_storage import FileStorage
from typing import TextIO
import unittest


def test_delete_file_method(file_path: str):
    """Removes a file if it exists."""
    if os.path.isfile(file_path):
        os.unlink(file_path)


def test_reset_store_method(store: FileStorage, file_path='file.json'):
    """Resets the items in the given store."""
    with open(file_path, mode='w') as f:
        f.write('{}')
        if store is not None:
            store.reload()


def test_read_text_file_method(file_name):
    """Reads the contents of a given file."""
    strings = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as f:
            for line in f.readlines():
                strings.append(line)
    return ''.join(strings)


def test_write_text_file_method(file_name, text):
    """Writes a text to a given file."""
    with open(file_name, mode='w') as f:
        f.write(text)
