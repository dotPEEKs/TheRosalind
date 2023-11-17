import time
import random
import struct
import base64
from lib.security.secure_random import generate_secure_bytes
from lib.security.hashing import HMAC
class KeygenFormat:
    KEYGEN_START_OF_KEYFILE = b" "*5 + b"-"*5 +  b"START-OF-KEYGEN-FILE" + b"-"*5
    KEYGEN_END_OF_KEYFILE = b" "*5 + b"-"*5 + b"END-OF-KEYGEN-FILE" + b"-"*5
    KEYGEN_STRUCT_FORMAT = ">I"
    @classmethod
    def validate_format(cls,input_: bytes) -> bool:
        if input_.startswith(cls.KEYGEN_START_OF_KEYFILE) and input_.startswith(cls.KEYGEN_END_OF_KEYFILE): # Burayı fixle 2.argüman endswith olmalı
            return True
        return False
    @classmethod
    def pack_key(cls,key: bytes,iv: bytes) -> bytes:
        hmac = HMAC()
        key_size = len(key)
        iv_size = len(iv)
        obfuscate_phase_1 = generate_secure_bytes(2048)
        obfuscate_phase_2 = generate_secure_bytes(250)
        obfuscate_phase_3 = generate_secure_bytes(1024)
        final_data = struct.pack(cls.KEYGEN_STRUCT_FORMAT,len(obfuscate_phase_1)) + obfuscate_phase_1 + struct.pack(cls.KEYGEN_STRUCT_FORMAT,key_size) + key + struct.pack(cls.KEYGEN_STRUCT_FORMAT,len(obfuscate_phase_2)) + obfuscate_phase_2 + struct.pack(cls.KEYGEN_STRUCT_FORMAT,iv_size) + iv + obfuscate_phase_3
        hmac.msg = final_data
        final_data = base64.b64encode(hmac.key + final_data + hmac.out)
        out = b""
        total_size = len(final_data)
        counter = 0
        while counter < total_size:
            out +=final_data[counter:counter+64] + b"\n"
            counter+=64
        return cls.KEYGEN_START_OF_KEYFILE + b"\n" + out + b"\n" + cls.KEYGEN_END_OF_KEYFILE

class QimageFormat:
    QIMG_START_FILE_HEADER = b"Qimg"
    QIMG_STRUCT_FORMAT = "<Q"
