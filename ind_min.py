def ind_min(sekwencja, pocz, kon):
    indeks=pocz
    a=sekwencja[pocz]
    for i in range(pocz,kon+1):
        if a>sekwencja[i]:
            indeks=i
    return indeks
print(ind_min("pies", 0, 3))
