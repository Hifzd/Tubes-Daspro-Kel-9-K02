from additional import pjglist

def hapusjin(arr) :
    arraybaru = []
    if pjglist(arr) == 0 :
        print("Tidak ada jin yang bisa dihilangkan")
    else :
        username = input('Masukkan jin yang ingin dihapus : ')
        if cek(arr,username) == False :
            YorN = input("Apakah kamu ingin menghapus jin "+username+" Y/N ?")
            if YorN == "Y" :
                for i in range(pjglist(arr)) :
                    if arr[i][0] != username :
                        arraybaru += [[arr[i][0],arr[i][1],arr[i][2]]]
            else :
                arraybaru = arr
        else :
            print("Tidak ada jin "+username)
            arraybaru = arr
    print(arraybaru)
    return arraybaru