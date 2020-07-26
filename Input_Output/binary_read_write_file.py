# ==================================
# writing data in binary mode
# converting the data into bytes format before writing to file.
# bw - b denotes binary mode, w denotes write mode
# to write to binary file we need to use file pointer and call write method
# in case of integer we need to call bytes method to convert the data to bytes format.
# otherwise you get error message a bytes-like object is required, not int
# ==================================
#
# with open("binary", "bw") as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))

# ********************************
# In actual, you wouldn't do it using for loop instead use range itself.
# print(bytes(range(0,17)));


# ==================================
# reading binary file in binary mode
# br - b denotes binary mode, r denotes read moe
# ==================================
# with open("binary", "br") as bin_file:
#     for b in bin_file:
#         print(b)


# ===================================
# we are going to convert large numbers into bytes.
# (2, 'big') or (4, 'big') or (4, 'little')
# first value is bytes information
# second value is whether we want it in "big indian" or "little indian" format
# big indian stores most significant bytes first and then the numbers
# little indian stores the least significant bytes first.
# ===================================

# a = 65534  # hex value FF FE
# b = 65535  # hex value FF FF
# c = 65536  # hex value 00 01 00 00 (4 bytes)
# d = 2998302  # hex value 02 2D C0 1E (4 bytes)
#
# with open("binary2", "bw") as binary2_file:
#     binary2_file.write(a.to_bytes(2, 'big'))
#     binary2_file.write(b.to_bytes(2, 'big'))
#     binary2_file.write(c.to_bytes(4, 'big'))
#     binary2_file.write(d.to_bytes(4, 'big'))
#     binary2_file.write(d.to_bytes(4, 'little'))

# ===================================
# we are going to read the binary file created from previous code.
# so here
#   e represents a
#   f represents b
#   g represents c
#   h represents d
#   i represents d again for little indian
# ===================================
with open("binary2","br") as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)  # output gives 515910912 value instead of 2998302 as we saved it in little indian adn reading it in big indian form.
