#1-girilen sayını 0-100 arasında olupolmadığını kontrol edınız
sayi=float(input("sayı: "))
result=(sayi> 0)  and (sayi<=100)
print(f'sayi 0-100 arasında mı: {result}')
#2-girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
#3- email ve parola bilgileri ile giris kontrolü yapınız
#4- girilen sayıyı büyüklük olarak kıyasayınız
#5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalmasını hesaplayınuz
#   eğer ortalama 50 ve üstü ise geçti değil ise kaldı yazdırınız
#a-) ortalama 50 ve üstünde olsa bile final notu en az 50 olmalıdır
#b-) finalden 70 alındığında ortalamanın önemi olmasın
#6- kişinin ad ,kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız
#  (formül= kilo/boy uzunluğunun karesi)
# asagıdakı tabloya göre kişi hangi gruba girmektedir
# 0-18.4=> zayıf
# 18.5-24.9=> normal
# 25.0-29.9=> fazla kilolu
#30.0-34,9=> şişman