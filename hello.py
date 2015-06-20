print "Hello!";

a = 1;
b = 2;
print a + b;

word = "abcdef";
a = word[1];
print a;
b = word[:3];
print b;
c = word[-1];
print c;
l = len(word);
print l;

# Multi-way decision
x = int(raw_input("Please enter an integer:"));
if x < 0:
	x = 0;
	print "Negative changed to zero!"
elif x == 0:
	print "Zero!"
else:
	print "More"

#loops List
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)

# Define and invoke function.
def sum(a,b):
    return a+b

func = sum
r = sum(5, 6)
r = func(2, 3)
print r

# The range() function
a =range(5,10)
print a
a = range(-2,-7)
print a
a = range(-7,-2)
print a
a = range(-2,-11,-3) # The 3rd parameter stands for step
print a

# file
spath="./test.txt"
f=open(spath,"w") # Opens file for writing.Creates this file doesn't exist.
f.write("First line 1.\n")
f.writelines("First line 2.")
f.close()

f=open(spath,"r") # Opens file for reading
for line in f:
    print line
f.close()

s=raw_input("Input your age:")
if s =="":
    raise Exception("Input must no be empty.")

try:
    i=int(s)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unknown exception!"
else: # It is useful for code that must be executed if the try clause does not raise an exception
    print "You are %d" %i,"years old"
finally: # Clean up action
    print "Goodbye!"
