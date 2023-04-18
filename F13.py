from additional import splitter
import os

def valid(folder):
    if os.path.isdir(folder):
        f = open(f'{folder}/user.csv', 'r')
        f.close()
        print('''Loading...

Selamat datang di program “Manajerial Candi”
Silahkan ketik login dan masukkan username Anda''')
        return True
        
    else:
        if folder == "":
            print('''Tidak ada nama folder yang diberikan!

Usage: python main.py <nama_folder>''')
        else :
            print(f'Folder "{folder}" tidak ditemukan.')
        return False

def load(folder, csv):
    dat = open(f'{folder}/{csv}', 'r')
    matrix = splitter(dat.read(), '\n')
    dat.close()
    return matrix
