''' List methods '''
mylist=[83, 2, 3]
print(len(mylist))
print(min(mylist))
print(sum(mylist))
print(sorted(mylist))
print(mylist)

mylist[0] = 8

del mylist[0]
print(mylist)


# listVar.reverse() vs. reversed(listVar)
# reverse the listVar using listVar.reverse()
# don't reverse the listVar using reversed(listVar)

# a list of elements from 1 to 10
a = list(range(1, 11))
print(a)

a.reverse()
print(a)


for i in reversed(a):
  print(i) 
print(a)

# list comprehension
import os

dirname='.'
dirlist='\n'.join([f for f in os.listdir(dirname) 
    if os.path.isdir(os.path.join(dirname, f))])
print('\n--- directory ---\n{}'.format(dirlist))

filelist='\n'.join([f for f in os.listdir(dirname) 
    if os.path.isfile(os.path.join(dirname, f))])
print('\n--- files ---\n{}'.format(filelist))
