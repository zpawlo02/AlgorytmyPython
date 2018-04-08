def f(x):
    return abs(x-2)
def calkowanie(f,a,b,n):
    wynik=0
    h=(b-a)/n
    for i in range(n):
        x1=a+i*h
        x2=x1+h
        y1=f(x1)
        y2=f(x2)
        wynik+=h*((y1+y2)/2)
    return wynik

print(calkowanie(f,0,5,5))
