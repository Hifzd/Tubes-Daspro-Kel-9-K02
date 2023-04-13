# File: main.py
from F13 import load
import commands
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan
userdata = ['' for i in range (3)]

users = load(args.folder, 'user.csv')
candi = load(args.folder, 'candi.csv')
bahan_bangunan = load(args.folder, 'bahan_bangunan.csv')

while True:
  masukan = input(">>> ")
  if masukan == 'exit':
    break
  else:
    commands.run(masukan, users, candi, bahan_bangunan, userdata)
    print()