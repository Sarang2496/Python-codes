# struct is the way to extract data and convert it to bytes format

# Why? 1 s and 0s to something human readable

from struct import *

# store as bytes data

packed_data = pack('iif', 6, 29, 4.78) # format and list of values

print(packed_data)

print(calcsize('i'))

print(calcsize('f'))
print(calcsize('iif'))

# to get data back to normal 
original_data =unpack('iif', packed_data)
print (original_data)
print (unpack('iif', b'\x06\x00\x00\x00\x1d\x00\x00\x00\xc3\xf5\x98@'))