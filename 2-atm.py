kullanicilar=[
    { 
        "name":"Berivan",
        "username":"berivan",
        "şifre":"123",
        "bakiye":20000
    },

    {
        "name":"mizgin",
        "username":"mizgin47",
        "şifre":"1234",
        "bakiye":15000
    },
      
    {
        "name":"kerem",
        "username":"kerem47",
        "şifre":"4380",
        "bakiye":19
    },  

]


hak=3

while True:
    kullanici=input("Kullanıcı Adınızı Giriniz:")

    for user in kullanicilar:
        if user["username"]==kullanici:
            password=input("Lütfen Şifrenizi Tuşlayınız:")
            while hak>0:
                if user["sifre"]==password:
                    print(user["name"]," Hoşgeldin")
                else:
                    hak=hak-1
                    print(hak)

            if hak==0:
                print("hesabınız bloke edildi")
                break

