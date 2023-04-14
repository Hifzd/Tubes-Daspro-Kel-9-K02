from additional import splitter

def valid(folder):
    if not(EOFError(open(f'{folder}/user.csv', 'r'))):
        print('''Loading...
    Selamat datang di program “Manajerial Candi”
    Silahkan masukkan username Anda''')
        return True
    else:
        print(f'Folder “{folder}” tidak ditemukan.')
        return False

def load(folder, csv):
    dat = open(f'{folder}/{csv}', 'r')
    matrix = splitter(dat.read(), '\n')
    return matrix
