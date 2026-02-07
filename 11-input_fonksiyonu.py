isim = input("Adın ne? ")
print("Memnun oldum", isim)

yas = input("Kaç yaşındasın? ")
print(yas + 5)

yas = int(input("Kaç yaşındasın? "))
print("5 yıl sonra yaşın:", yas + 5)

sayi = int(input("Tahmin et: Ben kaç sayısını tuttum? "))
print(sayi == 7)

yemek = input("Ne yemek istersin? (pizza / hamburger): ")

if yemek == "pizza":
    print("Pizza 75 TL!")
elif yemek == "hamburger":
    print("Hamburger 60 TL!")
else:
    print("Menüde o yok :)")

print("Mini Hesap Makinesine Hoşgeldiniz!")
sayi1 = int(input("Birinci sayıyı gir: "))
sayi2 = int(input("İkinci sayıyı gir: "))
islem = input("İşlem seç (+, -, *, /): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    print("Sonuç:", sayi1 / sayi2)
else:
    print("Geçersiz işlem!")

if yas < 13:
    print("Sen bir çocuksun! 🍭")
elif yas < 18:
    print("Gençsin! ⚡")
else:
    print("Yetişkisin! 💪")