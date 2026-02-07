from random import randint

tutulan_sayi=randint(1,10)
hak=3

while True:
    tahmin_sayi=int(input("1-10 Arasında Sayı Tahminizi Yazınız:"))
    hak=hak-1
    if hak==0:
        print("hakkınız kalmadı")
        print(tutulan_sayi)
        break
    else:
        
        if tutulan_sayi==tahmin_sayi:
             print("tahminiz doğru Tebrikler")
             break
        elif tutulan_sayi>tahmin_sayi:
            print("daha büyük bir sayı giriniz")
        elif tutulan_sayi<tahmin_sayi:
            print("daha küçük bir sayı giriniz")
        print(hak,"hakkınız kaldı")

    

