import ctypes

ctypes.CDLL('./libxl.so')

# Load the shared library
mycppmodule = ctypes.CDLL('./test.so')

# Define the return type of the C++ function
mycppmodule.get_string.restype = ctypes.c_char_p

# Define the argument type for the C++ function (string)
mycppmodule.get_string.argtypes = [ctypes.c_char_p]

def get_cpp_string(input_string):
    # Encode the input string as UTF-8
    input_bytes = input_string.encode('utf-8')
    
    # Call the C++ function with the encoded input
    return mycppmodule.get_string(input_bytes).decode('utf-8')
