# str and byte are two data types, dont mix them up!

b = b'abcd\x65';

print(b, b[0])


# convert to a mutable type
ba = bytearray(b)

# ba[0] = b'\x66'; // error
ba[0] = 102
print(ba)



# string is encoded to byte
s = '深入Python'
print(len(s))

b = s.encode('utf-8')
print(len(b))

b = s.encode('big5')
print(len(b))

# byte is decoded to string
t = b.decode('big5')
print(s == t)
