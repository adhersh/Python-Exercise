a= int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))

if a>b:
    if b>c:
        print(a,"is the greatest")
    else:
        if a>c:
            print(a,"is the greatest")
        else:
            print(c,"is the greatest")
else:
    if b>c:
        print(b,"is the greatest")
    else:
        print(c,"is the greatest")
        
""" using and elif
 """        
a= int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))

if a>b and a>c:
    print(a,"is the greatest")
elif b > a and b>c:
    print(b,"is the greatest")
else:
    print(c,"is the greatest")