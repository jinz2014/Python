# Not supported in P2.7

'''
input source being read could be anything: a web page, a string in memory, even the output of another program.  As long as your functions take a stream object and simply call the object's read() method, you can handle any input source that acts like a file, without specific code to handle each kind of input.
'''


import io

a_string = 'string is characters while byte is byte'
a_file = io.StringIO(a_string)
print(a_file.read())

print(a_file.seek(0))
print(a_file.read(10))
print(a_file.tell())

print(a_file.seek(18))
print(a_file.read())

