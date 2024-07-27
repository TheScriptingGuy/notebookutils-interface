from fsspec.implementations.arrow import ArrowFSWrapper
from pyarrow import fs
from pyarrow.fs import LocalFileSystem

from notebookutils.mssparkutils.handlers.fsHandler import FileInfo


def help(method_name=None):
    pass

def mountToDriverNode(source, mountPoint, extraConfigs={}):
    return False

def unmountFromDriverNode(mountPoint):
    return False

def mount(source, mountPoint, extraConfigs={}):
    return False

def unmount(mountPoint, extraOptions={}):
    return False

def mounts(extraOptions={}):
    return False

def refreshMounts():
    return False

def getMountPath(mountPoint, scope=""):
    return False

def fastcp(src, dest, recurse=True, extraConfigs={}):
    return False

def get_filesystem() -> tuple[LocalFileSystem, ArrowFSWrapper]:
    local = fs.LocalFileSystem()
    
    return (local,ArrowFSWrapper(local))
    
def ls(path):
    local, arrowfssystem = get_filesystem()
    pa_file_info_list= local.get_file_info(fs.FileSelector(path, recursive=False))
    
    custom_file_info_list = [
        FileInfo(file_info.path, file_info.size)
        for file_info in pa_file_info_list
    ]

    return custom_file_info_list

def mv(source_file_or_directory,destination_file_or_directory):
    """
    Moves a file or directory to a new location.
    :param source_file_or_directory: The source file or directory to move.
    :type source_file_or_directory: str
    :param destination_file_or_directory: The destination file or directory.
    :type destination_file_or_directory: str
    """
    local, arrowfssystem = get_filesystem()
    
    local.mv(source_file_or_directory, destination_file_or_directory)
    print(f"Moved {source_file_or_directory} to {destination_file_or_directory}")

def put(file_path, content, overwrite=False):
    """
    Writes content to a file.
    :param file_path: The path to the file to write.
    :type file_path: str
    :param content: The content to write to the file.
    :type content: str
    :param overwrite: Whether to overwrite the file if it already exists.
    :type overwrite: bool
    """
    local, arrowfssystem = get_filesystem()
    if arrowfssystem.exists(file_path) and overwrite == False:
        raise FileExistsError(f"{file_path} already exists. Set 'overwrite=True' to overwrite the file.")
    else:
        with local.open_output_stream(file_path) as f:
            f.write(content.encode('utf-8'))
        print(f"Wrote content to {file_path}")

def exists(file_path):
    """
    Checks if a file exists.
    :param file_path: The path to the file to check.
    :type file_path: str
    :return: True if the file exists, False otherwise.
    :rtype: bool
    """
    local, arrowfssystem = get_filesystem()
    return arrowfssystem.exists(file_path)

def append(file_path, content, create_if_not_exists=False):
    """
    Appends content to a file.
    :param file_path: The path to the file to append.
    :type file_path: str
    :param content: The content to append to the file.
    :type content: str
    :param create_if_not_exists: Whether to create the file if it does not exist.
    :type create_if_not_exists: bool
    """
    local, arrowfssystem = get_filesystem()
    if arrowfssystem.exists(file_path) and create_if_not_exists == False:
        raise FileExistsError(f"{file_path} doesn't exist. Set 'create_if_not_exists=True' to create the file.")
    else:
        with local.open_append_stream(file_path) as f:
            f.write(content.encode('utf-8'))
        print(f"Appended content to {file_path}")

def mkdirs(path):
    """
    Creates a directory and any necessary parent directories.
    :param path: The path to the directory to create.
    :type path: str
    """
    local, arrowfssystem = get_filesystem()
    arrowfssystem.mkdirs(path)
    print(f"Created directory {path}")

def cp(source_file_or_directory, destination_file_or_directory, recursive=False):
    """
    Copies a file or directory to a new location.
    :param source_file_or_directory: The source file or directory to copy.
    :type source_file_or_directory: str
    :param destination_file_or_directory: The destination file or directory.
    :type destination_file_or_directory: str
    :param recursive: Whether to copy all files and directories recursively.
    :type recursive: bool
    """
    local, arrowfssystem = get_filesystem()
    arrowfssystem.copy(source_file_or_directory, destination_file_or_directory, recursive)
    print(f"Copied {source_file_or_directory} to {destination_file_or_directory}")

def rm(file_or_directory, recursive=False):
    """
    Removes a file or directory.
    :param file_or_directory: The file or directory to remove.
    :type file_or_directory: str
    :param recursive: Whether to remove all files and directories recursively.
    :type recursive: bool
    """
    local, arrowfssystem = get_filesystem()
    arrowfssystem.rm(file_or_directory, recursive)
    print(f"Removed {file_or_directory}")

def head(file_path, max_bytes=1024):
    """
    Reads the first few bytes of a file.
    :param file_path: The path to the file to read.
    :type file_path: str
    :param max_bytes: The maximum number of bytes to read.
    :type max_bytes: int
    :return: The first few bytes of the file.
    :rtype: bytes
    """
    local, arrowfssystem = get_filesystem()
    with local.open_input_stream(file_path) as f:
        return f.read(max_bytes)

