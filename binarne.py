def binarne(tab,x):
    l=0
    p=len(tab)

    while l<=p:
        sr=(l+p)//2
        if tab[sr]==x:
            return sr
        elif x<tab[sr]:
            p=sr-1
        else:
            l=sr+1
    
    return -1

print(binarne([1,2,3,4,5,45,54,65,67],54))
