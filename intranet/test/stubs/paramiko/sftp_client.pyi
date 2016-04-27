# Stubs for paramiko.sftp_client (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from paramiko.sftp import BaseSFTP
from paramiko.util import ClosingContextManager

b_slash = ... # type: Any

class SFTPClient(BaseSFTP, ClosingContextManager):
    sock = ... # type: Any
    ultra_debug = ... # type: Any
    request_number = ... # type: Any
    logger = ... # type: Any
    def __init__(self, sock): ...
    @classmethod
    def from_transport(cls, t, window_size=None, max_packet_size=None): ...
    def close(self): ...
    def get_channel(self): ...
    def listdir(self, path=''): ...
    def listdir_attr(self, path=''): ...
    def listdir_iter(self, path='', read_aheads=50): ...
    def open(self, filename, mode='', bufsize=-1): ...
    file = ... # type: Any
    def remove(self, path): ...
    unlink = ... # type: Any
    def rename(self, oldpath, newpath): ...
    def mkdir(self, path, mode=...): ...
    def rmdir(self, path): ...
    def stat(self, path): ...
    def lstat(self, path): ...
    def symlink(self, source, dest): ...
    def chmod(self, path, mode): ...
    def chown(self, path, uid, gid): ...
    def utime(self, path, times): ...
    def truncate(self, path, size): ...
    def readlink(self, path): ...
    def normalize(self, path): ...
    def chdir(self, path=None): ...
    def getcwd(self): ...
    def putfo(self, fl, remotepath, file_size=0, callback=None, confirm=True): ...
    def put(self, localpath, remotepath, callback=None, confirm=True): ...
    def getfo(self, remotepath, fl, callback=None): ...
    def get(self, remotepath, localpath, callback=None): ...

class SFTP(SFTPClient): ...
