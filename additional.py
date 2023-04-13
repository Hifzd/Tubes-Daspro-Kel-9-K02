def splitter (opfile, pemisah):
    if len(opfile) == 0:
        return []

    else:
        pemisah1 = '\n'
        pemisah2 = ';'
        count = 1
        for chr in opfile:
            if chr == pemisah:
                count += 1
        
        baris = ["" for i in range(count)]
        i = 0

        for chr in opfile:
            if chr == pemisah:
                i+=1
            else:
                baris[i] += chr

        if pemisah == pemisah1:
            return [splitter(baris[i], ';') for i in range(len(baris))]
        else:
            return baris

def konso(lis, value):                             # Memasukkan elemen baru ke dalam list
    lis[len(lis):] = [value]
    return lis

def pjglist(lis):
    listring = str(lis)
    count = 0
    if len(listring) == 2:
        return 0
    else:
        if listring[1] == '[':
            for i in range(1,len(listring)):
                if listring[i] == '[':
                    count += 1
            return count
        else:
            for i in range(1,len(listring)):
                petik = 0
                if listring[i] == "'":
                    if petik == 1:
                        petik = 0
                    else:
                        petik = 1
                if listring[i] == ',' and petik == 0:
                    count += 1
            return count + 1
            