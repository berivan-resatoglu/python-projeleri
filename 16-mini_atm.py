kullanicilar={
    "kerem":{"sifre":"123","bakiye":160000},
    "berivan":{"sifre":"6057","bakiye":20000},
    "mizgin":{"sifre":"1946","bakiye":10000}
}
username=input("kullanıcı isminizi giriniz")
if username in kullanicilar:
    hak=3
    while hak>0:
        sifre=input("şifrenizi giriniz")
        if sifre==kullanicilar[username]["sifre"]:
            print("hesaba giriş yapıldı" )
            break
        else:
            print("sifreniz yanlış")
            hak=hak-1
    if hak==0:
        print("kartınız bloke olmuştur  hayırlı uğurlu olsun")
    else:
        
        print("""
        (1) bakiye görüntüle
        (2) para çek
        (3)para yatırma
        (4) çıkış
        
        """)
        secim=input("seçimizi yapınız:")
        if secim=="1":
            bakiye=kullanicilar[username]["bakiye"]
            print(bakiye)
        elif secim=="2":
            miktar=int(input("Ne kadar para çekimi yapmak istiyorsunuz ?"))
            bakiye=kullanicilar[username]["bakiye"]
            if miktar<=bakiye:
                bakiye=bakiye-miktar
                print("kalan bakiyeniz:",bakiye)
            else:
                print("bakiyeniz yeterli değil")
        elif secim=="3":
            bakiye=kullanicilar[username]["bakiye"]
            miktar=int(input("kaç  para yatırıcaksınız:"))
            bakiye=bakiye+miktar
            print("toplam bakiyeniz", bakiye)
        elif secim=="4":
            print("güle güle" )












