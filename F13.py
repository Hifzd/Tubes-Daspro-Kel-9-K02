from additional import splitter

def valid(folder):
    a = open(f'{folder}')
    if EOFError(a) and len(folder) > 0:
        print(f'Folder “{folder}” tidak ditemukan.')
        return False
    elif EOFError(a) and len(folder) == 0:
        print(f'Tidak ada nama folder yang diberikan!')
        print()
        print('Usage: python main.py <nama_folder>')
        return False
    else:
        print('''Loading...
Selamat datang di program “Manajerial Candi”
Silahkan masukkan username Anda''')

        return True

def load(folder, csv):
    dat = open(f'{folder}/{csv}', 'r')
    matrix = splitter(dat.read(), '\n')
    return matrix
