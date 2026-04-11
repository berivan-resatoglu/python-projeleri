#1-girilen sayını 0-100 arasında olupolmadığını kontrol edınız
sayi=float(input("sayı: "))
result=(sayi> 0)  and (sayi<=100)
print(f'sayi 0-100 arasında mı: {result}')
#2-girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
sayi=int(input("sayi: "))
result=(sayi>0) and (sayi%2==0)
print(f' girilen sayi pozitif çift sayı mı : {result}')
#3- email ve parola bilgileri ile giris kontrolü yapınız
email="email@berivan"
password="abc123"
girilenemail=input("email: ")
girilenpassword=input("password: ")
result(girilenemail==email) and(girilenpassword==password)
print(f"uygulamaya giriş başarılı mı : {result}")

#4- girilen sayıyı büyüklük olarak kıyasayınız
a =int(input("a : "))
b =int(input("b : "))
c =int(input("c : "))
result=(a>b) and (a>b)
print(f"a en büyük sayıdır : {result}")
result =(c>a) and (c>b)
print(f"b en büyük sayıdır : {result}")
result=(b>a) and (b>c)
print(f"b en büyük sayıdır : {result}")
#5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalmasını hesaplayınuz
#   eğer ortalama 50 ve üstü ise geçti değil ise kaldı yazdırınız
#a-) ortalama 50 ve üstünde olsa bile final notu en az 50 olmalıdır
#b-) finalden 70 alındığında ortalamanın önemi olmasın

vize1=float(input("vize1: "))
vize2=float(input("vize2: "))
final=float(input("final: "))
ortalama=((vize1+vize2)/2)*0.6+ (final*0.4)
result=(ortalama >=50) and (final>=50)
result=(ortalama >=50) or (final>=70)
print(f"öğrencinin ortalaması {ortalama} ve geçme durumu : {result}")
#6- kişinin ad ,kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız
#  (formül= kilo/boy uzunluğunun karesi)
# asagıdakı tabloya göre kişi hangi gruba girmektedir
# 0-18.4=> zayıf
# 18.5-24.9=> normal
# 25.0-29.9=> kilolu
#30.0-34,9=> şişman

name =input ("adınız :")
kg:float("kilonuz :")
hg=float(input("boyunuz :"))
index =(kg)/(hg**2)
zayif=(index>=0)and (index<=18.4)
normal=(index>=18.4)and (index<=24.9)
kilolu=(index>24.9)and (index<=29.9)
şişman=(index>=30.0)and (index<=34.9)
print(f"(name) kilo indeksin :{index} ve kilo değerlendirmen zayıf:{zayif}")
print(f"(name) kilo indeksin :{index} ve kilo değerlendirmen normal:{normal}")
print(f"(name) kilo indeksin :{index} ve kilo değerlendirmen kilolu:{kilolu}")
print(f"(name) kilo indeksin :{index} ve kilo değerlendirmen şişman:{şişman}")


