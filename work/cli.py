import sys
print('sys.argv',sys.argv)
if len(sys.argv)<2:
    print('need 2 params')
    exit(1)
else:
    print('args are',sys.argv[1:])
a,b=sys.argv[1:3]
if a.isnumeric() and b.isnumeric():
    print("product is:",int(sys.argv[1])*int(sys.argv[2]))
else:
    print('not numeric')