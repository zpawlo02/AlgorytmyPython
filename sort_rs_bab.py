def zamien(lista, i, j):
    a=lista[i]
    b=lista[j]
    lista[i]=b
    lista[j]=a
    

def sort_rs_bab(t):
    for i in range(len(t)-1,0,-1):
        for j in range(i): 
            if t[j]>t[j+1]:
                zamien(t,j,j+1) 
    return t

print(sort_rs_bab([7,34,16,8,0,11,3,12,23]))

                
