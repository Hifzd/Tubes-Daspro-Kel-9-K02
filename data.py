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
    
def load(filename, matrix):
    dat = open(filename, 'r')
    matrix = splitter(dat.read(), '\n')
    return matrix
