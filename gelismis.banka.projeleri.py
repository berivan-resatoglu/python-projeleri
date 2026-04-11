import json #json modülünü import eder
import random #random modülünü import eder

with open("bankamatik.json" , "r" , encoding="utf-8") as file: #bankamatik.json dosyasını okur ve json formatına çevirir    
    data =json.load(file) #json formatına çevirilen dosyayı data değişkenine atar

    while True:
        mail=input("mail adresinizi giriniz:") #mail adresini kullanıcıdan alır
        giris=False
        for user in data: #data değişkeninin her bir elemanını alır ve yazdırır
            if user["mail"]==mail: #mail adresi data değişkeninin her bir elemanının mail adresi ile eşleşiyorsa
                password=input("sifresini giriniz:") 
                if user["sifre"]==password:
                    print("giris başarili")
                    giris=True
                    break
                else:
                    print("sifreniz yanlis")
                    giris=False
                    break
        if giris==False:
            secim=input(f"yeni kullanıcı olusturmak istiyor musunuz? (e/h):")
            
           
        if secim=="e":
              new_mail=input("mail adresinizi giriniz:")
              new_password=input("sifrenizi giriniz:")
              hesap_var=False
              for user in data:
                if user["mail"]==new_mail:
                    print("bu mail adresi zaten kullanılıyor")
                    hesap_var=True
                    break
                if hesap_var==True:
                    break
                else:
                    with open("bankamatik.json" , "w" ,encoding="utf_8") as file:
                        data.append({
                            "mail":new_mail,
                            "sifre":new_password,
                            "bakiye" :{
                                "TL":0,
                                "USD":0,
                                "EUR":0,
                                "GOLD":0
                            }
                        })        
                        json.dump(data,file, indent=4,ensure_ascii=False)
                        print("hesap")

