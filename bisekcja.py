def f(x):
    return (x**2-3)

def bisekcja(f,a,b,eps):
    c =(a+b)/2
    while(abs(f(c))>eps):
        c=(a+b)/2
        if (f(c)>0 and f(a)<0):
            b=c
        else:
            a=c
    return c
def bisekcja_rekurencja(f,a,b,eps):
    c=(a+b)/2
    if(f(c)>0 and f(a)<0):
        b=c
    else:
        a=c
    if(abs(f(c))>eps):
        return bisekcja_rekurencja(f,a,b,eps)
    else:
        return c

print(bisekcja_rekurencja(f,1,5,0.01))
print(bisekcja(f,-14,2,0.000001))
