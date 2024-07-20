import os


class FileInfo:
    def __init__(self, path, size):
        self.path = path
        self.name = os.path.basename(path)
        self.size = size

    def __repr__(self):
        return f"FileInfo(path={self.path}, name={self.name}, size={self.size})"