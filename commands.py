from F01 import login
from F02 import logout
from F03 import summonjin


def run(masukan, users, candi, bahan_bangunan, userdata):
    if masukan == 'login':
        userdata = login(userdata, users)
    elif masukan == 'logout':
        userdata = logout(userdata)
    elif masukan == 'summonjin':
        if userdata[2] == "bandung_bondowoso":
            users = summonjin(users)