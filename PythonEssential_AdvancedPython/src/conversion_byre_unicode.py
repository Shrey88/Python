""" *
    *   you can decode the byte characters to unicode and vis-a-versa
    *
    *   bytes and strings are not same and you need to take care of it separately
    * """

b = bytes([0x41, 0x42, 0x43, 0x44])  # <-- byte codes
print(b.decode('UTF-8'))  # <-- decoding it in UTF-8 format


s = "This is a string"
print(s.encode('UTF-8'))