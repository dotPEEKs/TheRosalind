import string
import base64
from lib.io.IO import IO
from lib.security.secure_random import generate_secure_bytes
from lib.security.hashing import PBDKF2
from lib.errno import *
from lib.format.formats import KeygenFormat
from lib.others.random_char_gen import generate_random_char
errno_wrapper = ErrorWrapper(show=True)

class Keygen(KeygenFormat):
    def __init__(self):
        self._key = PBDKF2().key
        self._iv = generate_secure_bytes(16)
    @classmethod
    @errno_wrapper.error_wrap
    def import_key(cls,input_data):
        if hasattr(input_data,"fd") and input_data.fd.readable():
            data = input_data.read()
        elif isinstance(input_data,bytes):
            data = input_data
        else:
            return ERRNO.BAD_DATA_TYPE
        start_offset = len(cls.KEYGEN_START_OF_KEYFILE)
        end_offset = len(data) - len(cls.KEYGEN_END_OF_KEYFILE)
        cls.data = input_data[start_offset:end_offset]
        return cls
    def export_key(self):
        filename = generate_random_char(lenght=16) + ".Qkeygen"
        content = self.pack_key(self._key,self._iv)
        if IO.create_file(fname=filename) == SUCCESNO.GOOD_CREATE_FILE:
            with IO(filename,"wb") as fd:
                fd.write(content)