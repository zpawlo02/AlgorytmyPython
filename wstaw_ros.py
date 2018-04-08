def wstaw_ros(lista, element, pocz, kon):
    for i in range(pocz,kon+1):
        if lista[i]<=element and lista[i+1]>element:
            lista.insert(i+1,element)
    

def sort_ros_wst(t):
    for i in range(len(t)-1):
        wstaw_ros(t,t[len(t)-1],0,i)
        t.pop()
        
    return t

print(sort_ros_wst([4,3,67,54,6]))

def sort_ros(t):
    for i in range(len(t)-1):
        t.(len(t)-1)
        
    
