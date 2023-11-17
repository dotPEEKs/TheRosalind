import time
import warnings

from enum import Enum
#__all__ = ["ERRNO","translate_errno_msg","Errno"] # we defining at here only required functions or classes 

errornum = Enum
class NumCounter:
    """
    It's countering for Errno

    when use this class automaticly will increase the counter and you dont need to edit to counter
    
    usage:
    
    Errno = NumCounter()
    
    class Employee(Enum):
    
        ERRNO_ERRNO_NUM_1 = Errno()
        
        ERRNO_ERRNO_NUM_2 = Errno()
    """
    def __init__(self):
        self.counter = 0
    def __call__(self):
        self.counter = self.counter + 1
        return self.counter
    def __repr__(self):
        return "<(%s val = %s)" % (self.__class__.__name__,self.counter)
Errno = NumCounter()
class ERRNO(Enum):
    #INVALID SECTOR
    INVALID_ERRNO_NUM = Errno()

    INVALID_FILE_TYPE = Errno()
    INVALID_FILE_MODE = Errno()
    INVALID_KEYGEN_FILE = Errno()
    # BAD SECTOR
    
    BAD_PERMISSION = Errno()
    BAD_FILE_MODE = Errno()
    BAD_DATA_TYPE = Errno()
    BAD_FD_DESCRIPTOR = Errno()
    BAD_KEYGEN_FILE_FORMAT = Errno()
    # ERRNO SECTOR
    
    ERRNO_EXISTING_FILE = Errno()
    ERRNO_NON_EXISTING_FILE = Errno()
    ERRNO_NON_READABLE_FILE = Errno()
    ERRNO_NON_WRITABLE_FILE = Errno()


SuccesNo = NumCounter()
class SUCCESNO(Enum):
    GOOD_CREATE_FILE = SuccesNo()


def translate_errno_msg(msg: ERRNO) -> str:
    msg_tables = {
        ERRNO.BAD_FILE_MODE:"Bad file mode it's mean specified file mode doesnt support",
        ERRNO.BAD_PERMISSION:"Bad permission it mean you dont have required permission yet",
        ERRNO.BAD_FD_DESCRIPTOR:"Unsupported fd descriptor inputs fd's must be IO class",
        ERRNO.BAD_KEYGEN_FILE_FORMAT:"Bad key file format",
        ERRNO.INVALID_FILE_MODE:"Invalid File mode ",
        ERRNO.INVALID_FILE_TYPE:"Invalid file type only files can openable",

        ERRNO.INVALID_ERRNO_NUM:"Invalid Error number :)",
        ERRNO.ERRNO_EXISTING_FILE:"File already exists",
        ERRNO.ERRNO_NON_EXISTING_FILE:"Non existing file. File dont exist given path",
        ERRNO.ERRNO_NON_READABLE_FILE:"Non readable file. you cannot read file you can check file mode and try again",
        ERRNO.ERRNO_NON_WRITABLE_FILE:"Non writable file. you cannot read file you can check file mode and try again",

        # GOOD SECTOR

        SUCCESNO.GOOD_CREATE_FILE:"File Succesfully created :)"
    }
    if msg_tables.get(msg) is None:
        return msg_tables[ERRNO.INVALID_ERRNO_NUM]
    return msg_tables[msg]

class ErrorWrapper:
    def __init__(self,show = False):
        self.show = show
    def error_wrap(self,class_or_func):
        def wrapper(*args,**kwargs):
            start_msg = "A error occured"
            end_msg = "Error Code:"
            out = class_or_func(*args,**kwargs)
            if isinstance(out,errornum) and self.show:
                if str(out).startswith("SUCCESNO"):
                    start_msg = "Succes"
                    end_msg = "Succes Code: "
                print("%s [%s] TranslatedMsg(msg = %s) %s %s" % (
                    start_msg,
                    time.ctime(),
                    translate_errno_msg(out),
                    end_msg,
                    out
                ))
            return out
        return wrapper