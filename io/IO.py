import os
from lib.errno import *
from typing import AnyStr
wrapper = ErrorWrapper(show=True)
class IO:
    """
    For file reading and reading
    """
    @wrapper.error_wrap
    def __new__(cls,file: str,fmode: str):
        if not os.path.exists(file):
            return ERRNO.ERRNO_NON_EXISTING_FILE
        elif not os.path.isfile(file):
            return ERRNO.INVALID_FILE_TYPE
        try:
            cls.fd = open(file,mode=fmode)
        except ValueError: # bad file mode
            return ERRNO.BAD_FILE_MODE
        except PermissionError:
            return ERRNO.BAD_PERMISSION
        return super(IO,cls).__new__(cls)
    def __init__(self,file: str,fmode: str):
        self.fname = file
        self.fmode = fmode
        self.fsize = os.path.getsize(self.fname)
    @property
    def readable(self) -> bool:
        return self.fd.readable()
    
    @property
    def writable(self) -> bool:
        return self.fd.writable()
    
    @wrapper.error_wrap
    @staticmethod
    def create_file(fname: str):
        """
        For creating file
        usage:IO.create_file("test_file")
        """
        if os.path.exists(fname):
            return ERRNO.ERRNO_EXISTING_FILE
        try:
            file_fd = open(fname,"w")
            file_fd.close()
        except PermissionError:
            return ERRNO.BAD_PERMISSION
        return SUCCESNO.GOOD_CREATE_FILE
    @wrapper.error_wrap
    def read(self,buffer = None) -> AnyStr:
        """
        if you wanna can set buffer but buffer type must be int
        fd = IO("test_file.bin","rb")
        fd.read(buffer = 1881)
        """
        where_i_am = self.fd.tell()
        if where_i_am == self.fsize: # go to start of file
            self.fd.seek(0,os.SEEK_SET) #we are set current position to 0(start of file)
        if self.fd.readable():
            try:
                return self.fd.read(buffer)
            except:
                pass
        else:
            return ERRNO.ERRNO_NON_READABLE_FILE
    @wrapper.error_wrap
    def write(self,content: AnyStr,flush = False) -> AnyStr:
        if not self.fd.writable():
            return ERRNO.ERRNO_NON_WRITABLE_FILE
        try:
            self.fd.write(content)
            if flush:
                self.fd.flush() # dont wait data in buffer
        except TypeError: #wrong input data type
            return ERRNO.BAD_DATA_TYPE
        except Exception as unknown_data_error:
            pass # burayı düzelt
    @wrapper.error_wrap
    def read_buffered(self,buffer = None):
        readed = 0
        while readed < self.fsize:
            output = self.read(buffer)
            if isinstance(output,errornum):
                readed = self.fsize # break the loop
                yield output
            else:
                readed = readed + len(output)
                yield output
    def close(self):
        if not self.fd.closed:
            self.fd.close()
    def __enter__(self):
        return self
    def __exit__(self,*args,**kwargs):
        self.close()
    def __repr__(self):
        outstring = "<(%s = file_name = %s file_mode = %s can_readable = %s can_writable = %s)>" % (
            self.__class__.__name__,
            self.fname,
            self.fmode,
            "yes" if self.fd.readable() else "no",
            "yes" if self.fd.writable() else "no"
        )
        return outstring