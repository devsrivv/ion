# Stubs for paramiko.sftp_file (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from paramiko.file import BufferedFile

class SFTPFile(BufferedFile):
    MAX_REQUEST_SIZE = ... # type: Any
    sftp = ... # type: Any
    handle = ... # type: Any
    pipelined = ... # type: Any
    def __init__(self, sftp, handle, mode='', bufsize=-1): ...
    def __del__(self): ...
    def close(self): ...
    def settimeout(self, timeout): ...
    def gettimeout(self): ...
    def setblocking(self, blocking): ...
    def seek(self, offset, whence=0): ...
    def stat(self): ...
    def chmod(self, mode): ...
    def chown(self, uid, gid): ...
    def utime(self, times): ...
    def truncate(self, size): ...
    def check(self, hash_algorithm, offset=0, length=0, block_size=0): ...
    def set_pipelined(self, pipelined=True): ...
    def prefetch(self, file_size): ...
    def readv(self, chunks): ...
