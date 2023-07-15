#!/usr/bin/python3
"""Takes care of storage requirements"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
