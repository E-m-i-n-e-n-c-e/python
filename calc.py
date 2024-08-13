a=input("Enter the expression to be calculated:\n")
a=a.split(" ")
x=int(a[0])
y=int(a[2])
z=a[1]
if (z=="+"):
    print(x+y)
elif (z=="-"):
    print(x-y)
elif (z=="*"):
    print(x*y)
elif (z=="/"):
    print(x/y)
elif (z=="**"):
    print(x**y)
elif (z=="%"):
    print(x % y)
elif (z=="//"):
    print(x // y)
elif (z=="&"):
    print(x & y)
elif (z=="|"):
    print(x | y)
elif (z=="^"):
    print(x ^ y)
elif (z=="<<"):
    print(x << y)
elif (z==">>"):
    print(x >> y)
a=True
print(a)