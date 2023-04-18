from additional import pjglist

def konso(lis, value):
    pjgawal = pjglist(lis)
    lislam = lis
    lis = [0 for i in range(pjgawal+1)]                           # Memasukkan elemen baru ke dalam list
    for i in range(pjgawal):
        lis[i] = lislam[i]
    lis[pjgawal] = value
    return lis

# def konso(lis, value):                             # Memasukkan elemen baru ke dalam list
#     lis[len(lis):] = [value]
#     return lis

b = [['a','b'],['c','d']]
a = ['a','e']

b = konso(b,a)
print(b)