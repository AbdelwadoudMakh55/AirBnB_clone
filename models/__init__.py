#!/usr/bin/python3
"""This is the __init__ module creates a unique FileStorage instance for the
application
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
