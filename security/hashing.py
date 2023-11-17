import hmac
import hashlib
from .secure_random import generate_secure_bytes
from enum import Enum

class Algorithm:
    __allowed__algorithms__ = ["md5","sha1","sha256","sha384","sha512"]
    MD1 = "md1"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"
    @classmethod
    def algorithm_check(cls,algorithm) -> bool:
        return algorithm in cls.__allowed__algorithms__
class HMAC:
    """
    For Data checking and validating
    usage:
    hmac_handler = HMAC()
    hmac_handler.key = b"your_key_here" # you can use generate_secure_bytes but key must be bytes
    hmac_handler.msg = b"your secret msg" # for message changing and input data must be bytes
    hmac_handler.out # you can take output
    # Warning: But don't lost secret key this is your own responsibility not me and i dont take own any damages or data losts
    """
    def __init__(self):
        self._msg = b""
        self._key = generate_secure_bytes()
        self._algo = Algorithm.SHA256
    @property
    def key(self):
        return self._key
    @key.setter
    def key(self,hkey: bytes):
        if not isinstance(hkey,bytes):
            raise TypeError("HMAC Key must be bytes not %s " % (hkey.__class__.__name__))
        elif len(hkey) < 32:
            raise ValueError("HMAC Key greater than 32 user input key size: %s" % (len(hkey)))
        self._key = hkey
    @property
    def msg(self):
        return self._msg
    @property
    def algo(self):
        return self._algo
    @algo.setter
    def algo(self,algorithm: Algorithm):
        """
        Warning:Algorithm type must be enum and must be have attribute
        Usage:
        hmac_handler = HMAC()
        hmac_handler.algo = Algo.ALGO_SHA512
        hmac_handler.out
        """
        if Algorithm.algorithm_check(algorithm):
            raise ValueError("Invalid algorithm or not allowed hash algorithm you can use only this algorithms: ","-".join(Algorithm.__allowed__algorithms__))
        self._algo = algorithm
    @msg.setter
    def msg(self,msg: bytes):
        if not isinstance(msg,bytes):
            raise TypeError("Input must be bytes not %s " % (msg.__class__.__name__))
        self._msg = msg
    @property
    def out(self) -> bytes:
        return hmac.new(self.key,self.msg,getattr(hashlib,self.algo)).digest()
    def __repr__(self) -> str:
        return "<(%s key = %s algorithm = %s msg = %s)>" % (
            self.__class__.__name__,
            self.key,
            self.algo,
            self.msg
        )
class PBDKF2:
    """
    It's generating SHA256 
    """
    def __init__(self):
        self._key_iter = 1000000
        self._salt = generate_secure_bytes()
        self._key = generate_secure_bytes()
        self._algo = Algorithm.SHA256 # default
    @property
    def key(self) -> bytes:
        return self._key
    @key.setter
    def key(self,pkey: bytes):
        if not isinstance(pkey,bytes):
            raise TypeError("PBDKF2 Key must be bytes not %s " % (pkey.__class__.__name__))
        self._key = pkey
    @property
    def algo(self):
        return self._algo
    @algo.setter
    def algo(self,algorithm: Algorithm):
        if not Algorithm.algorithm_check(algorithm):
            raise ValueError("Invalid algorithm %s you can use this algorithms %s" % (algorithm,"-".join(Algorithm.__allowed__algorithms__)))
        self._algo = algorithm
    @property
    def out(self):
        return hashlib.pbkdf2_hmac(self._algo,self._key,self._salt,self._key_iter)
    def __repr__(self) -> str:
        return "<(%s key = %s salt = %s key_iter = %s hash_algorithm = %s)>" % (
            self.__class__.__name__,
            self.key,
            self._salt,
            self._key_iter,
            self._algo
        )

