def nwd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif(a>=b):
        return nwd(b,a%b)
    elif(a<b):
        return nwd(a,b%a)
def nwdd(a,b):
    while(a!=0 and b!=0):
        if(a>b):
            a=a%b
        elif(a<b):
            b=b&a
    print(a+4)
    
nwdd(25,30)
