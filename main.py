# File: main.py
import F13
import commands
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder", default='', nargs='?')
args = parser.parse_args()

valid = F13.valid(args.folder)

# Anggap semua fungsi yang dipanggil mesrupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan
userdata = ['' for i in range (3)]

if valid:
  users = F13.load(args.folder, 'user.csv')
  candi = F13.load(args.folder, 'candi.csv')
  bahan_bangunan = F13.load(args.folder, 'bahan_bangunan.csv')

while valid:
  masukan = input(">>> ")
  if masukan == 'exit':
    break
  else:
    commands.run(masukan, users, candi, bahan_bangunan, userdata)
    print()