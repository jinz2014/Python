# tuple
print(type(5+3))
print(type(5+3,))

a=['jim', 30];
b=['yan', 32];
c=['tom', 42];

# a tuple composed of three lists
t = (a, b, c);

t[0][1] = 31;
print(a);

print(t);

# tuple is immutable, or more specifically,
# reference cannot be changed after 
# the tuple is created
a=['jim', 42];
print(t);



