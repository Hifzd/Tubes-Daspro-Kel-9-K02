# File: main.py
import F13
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

if F13.valid(args.folder):
  users = F13.load(args.folder, 'user.csv')
  candi = F13.load(args.folder, 'candi.csv')
  bahan_bangunan = F13.load(args.folder, 'bahan_bangunan.csv')
  
else:
  F13.error(args.folder)

while F13.valid:
  masukan = input(">>> ")
  if masukan == 'exit':
    break
  else:
    commands.run(masukan, users, candi, bahan_bangunan, userdata)
    print()