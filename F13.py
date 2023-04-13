from additional import splitter

def load(folder, csv):
    if EOFError() and folder == '':
        print('Tidak ada nama folder yang diberikan!')
        print('Usage: python main.py <nama_folder>')
    elif EOFError() and len(folder)!=0:
        print(f'Folder “{folder}” tidak ditemukan.')
    else:
        dat = open(f'{folder}/{csv}', 'r')
        matrix = splitter(dat.read(), '\n')
        return matrix