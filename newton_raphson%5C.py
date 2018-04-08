
def newton_raphson(a,b,eps):
    a=1
    p=b
    while(abs(a-b)>eps):
        a=(a+b)/2
        b=p/a
    return a
def new(a,b,eps):
    a=1
    p=b
    a=(a+b)/2
    b=p/a
    if(abs(a-b)>eps):
        return new(a,b,eps)
    else:
        return a
print(new(1,200,0.0000001))
