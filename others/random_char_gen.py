import string
import random
def generate_random_char(lenght=32):
    char_array =  string.ascii_letters + "1234567890"
    return "".join(random.sample(char_array,lenght))
