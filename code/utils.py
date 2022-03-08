from struct import unpack

def byte_to_int(byte_array) -> int:
    return unpack('b', byte_array)[0]

def bytes_to_string(byte_array) -> str:
    return byte_array.decode('utf8', errors='ignore')

def bytes_to_word(byte_array) -> int:
    return unpack('H', byte_array)[0]

def bytes_to_word_list(byte_array) -> list[int]:
    word_list = []
    for i in range(0, len(byte_array), 2):
        word_list.append(unpack('H', byte_array[i:i+2]))
    return word_list

def bytes_to_float(byte_array) -> float:
    return unpack('f', byte_array)[0]

def bytes_to_long(byte_array) -> int:
    return unpack('l', byte_array)[0]

def bytes_to_int_list(byte_array) -> list[int]:
    return  [b for b in byte_array]

"""bytes_to_dword() expects bytes of unsigned long length"""
def bytes_to_dword(byte_array) -> int:
    return unpack('L', byte_array)[0]
    # return int.from_bytes(byte_array, byteorder='little', signed=False)
    
def bytes_to_double(byte_array) -> int:
    return unpack('d', byte_array)[0]

def bytes_to_short(byte_array) -> int:
    return unpack('h', byte_array)[0]