def ind_min(sekwencja, pocz, kon):
    indeks=pocz
    a=sekwencja[pocz]
    for i in range(pocz,kon+1):
        if a>sekwencja[i]:
            indeks=i
    return indeks

def zamien(lista, i, j):
    a=lista[i]
    b=lista[j]
    lista[i]=b
    lista[j]=a
    
def sort_ros_w(t):
    a=0
    for i in range(len(t)):
        c=ind_min(t, i, len(t))
        zamien(t,a,c)
        a+=1
    return t

print(sort_ros_w([7,16,5,8,12]))
    
        
