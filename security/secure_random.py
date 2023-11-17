"""
Generating for securely random bytes
"""
import secrets
def generate_secure_bytes(n=None) -> bytes:
    """
    IT's generating secure random bytes default random byte is 32 if you wanna can change size
    """
    size = n if not n is None and isinstance(n,int) else 32
    return secrets.token_bytes(size)
