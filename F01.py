from additional import pjglist

def login(userdata,users):
    if userdata[0] == '':
        inpusr = input("Username : ")
        pwd = input("Password : ")
        print()

        for i in range(pjglist(users)):         #loop akan mengecek apakah inputan username dari user terdapat pada list "username"
            if users[i][0] == inpusr:          #jika terdapat username yang terdaftar pada list, maka loop akan diberhentikan
                userdata[0] = inpusr
                break            
        if userdata[0] == "":                           #jika username belum terdaftar pada list "username"
            print("Username tidak terdaftar")
        elif pwd != users[i][1]:                 
            print("Password salah!")
            userdata[0] = ""            #jika password salah, maka username pengguna di reset (dianggap belum login kembali)
            userdata[1] = ""
        else:
            #data username dan rolenya akan di simpan sebagai pengguna yang sedang login dalam sesi ini
            userdata[0], userdata[1], userdata[2] = inpusr, pwd, users[i][2]
            print(f"Selamat datang, {inpusr}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            return userdata
    else:
        print('Login gagal')
        print(f'Anda telah login dengan username {userdata[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.')
        return userdata