from additional import pjglist, konso

def summonjin(users):
    print('Jenis jin yang dapat dipanggil:')
    print(' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
    print(' (2) Pembangun - Bertugas membangun candi')
    print()
    while True:
        jenis = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
        print()
        if jenis == 1 or jenis == 2 :
            print('Memilih jin', end=" ")
            if jenis == 1 :
                rolejin = "jin_pengumpul"
                print('"Pengumpul".')
            else:
                rolejin = "jin_pembangun"
                print('"Pembangun".')
            break
        else:
            print(f'Tidak ada jenis jin bernomor "{jenis}"!')
    print()

    while True:
        usrnjin = input('Masukkan username jin : ')
        for i in range(pjglist(users)):
            if usrnjin == users[i][0]:
                print(f'Username "{usrnjin}" sudah diambil!')
                print()
                break
        if usrnjin != users[i][0]:
            break
        
    while True:
        pwdjin = input('Masukkan password jin : ')
        print()
        if len(pwdjin) < 5 or len(pwdjin) > 25:
            print('Password panjangnya harus 5-25 karakter!')
            print()
        else:
            break
    print('Mengumpulkan sesajen...')
    print('Menyerahkan sesajen...')
    print('Membacakan mantra...')
    print()
    jinbaru = [usrnjin, pwdjin, rolejin]
    #users.append(jinbaru)
    print(f'Jin {usrnjin} berhasil dipanggil')
    return konso(users, jinbaru)