import random
secenekler=["taş","kağıt", "makas"]
kullanici_skor=0
bilgisayar_skor=0
beraberlik=0


while kullanici_skor<3 and bilgisayar_skor<3:
    bilgisayar_secimi=random.choice(secenekler)
    kullanici_secimi=input("taş,kağıt,makas. secimini yap:").lower()
    
    while kullanici_secimi not in secenekler:
         kullanici_secimi=input("Hatalı giriş. taş,kağıt,makas seç(q ile çık)").lower()
         if kullanici_secimi=="q":
            print("oyundan çıkılıyor")
            break
    print(f"bilgisayar secimi:{bilgisayar_secimi}")#bunu anlamadım 

    if kullanici_secimi==bilgisayar_secimi:
        print("Berabere. Tekrar dene.")
        
    elif( kullanici_secimi== "taş" and bilgisayar_secimi=="makas") or (kullanici_secimi=="makas" and bilgisayar_secimi=="kağıt") or  (kullanici_secimi=="kağıt" and bilgisayar_secimi=="taş"):

        kullanici_skor+=1
        print("TEBRİKLEEEEEER SEN KAZANDIN🤜​🤛​")
    
    else:
        bilgisayar_skor+=1
        print("Bilgisayar kazandı😒​😒​")
    print(f"Skor → Sen: {kullanici_skor} | Bilgisayar: {bilgisayar_skor} | Berabere: {beraberlik}")
    print("-" * 40)#chatGPT burda ne demek istemiş bende bilmiyorum


    if kullanici_skor==3:
       print("TEBRİKLER SEN KAZANDIN💪​")
    elif bilgisayar_skor==3:

        print("bigisayar kazandı ama üzülme oyunda kaybeden aşkta kazanır ​🥰​")
        ##########BİLGİLENDİRME=KOPYA ÇEKMEDİM EKSİKLERİMİ CHATGPT DEN TAMAMLADIM AMA HALEN EKSİKLER VAR BENDEN BU KADAR HOCAM SİZ TAMAMLARSINIZ TEŞEKÜRLER:)






