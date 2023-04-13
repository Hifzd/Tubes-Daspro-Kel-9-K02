def logout(userdata):
    if userdata[0] == '':
        print("Logout gagal")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return userdata
    else:
        print("Berhasil logout")
        userdata[0], userdata[1], userdata[2] = "", "", ""
        return userdata