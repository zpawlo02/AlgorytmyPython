def wytnij(napis,pocz,kon,co_ile):
    pom=list(napis)
    elementy=[]
    for i in range(pocz, kon+1, co_ile):
        elementy.append(i)
        print(elementy)
    for i in range(len(elementy),0,-1):
        pom.pop(elementy[i-1])
        print(pom)
    return(''.join(pom))
print(wytnij("123456789",1,3,1))
