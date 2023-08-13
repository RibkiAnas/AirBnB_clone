#!/usr/bin/python3
"""
This module initializes the Storage Engine
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
