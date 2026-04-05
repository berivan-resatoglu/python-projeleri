sayilar=[1,3,5,7,9,12,19,21]
#1-sayilar listesindeki hangi sayılar 3 ün katıdır?
for sayi in sayilar:
    if (sayi%3==0):#sayi 3 ün katı mı diye kontrol eder
        print(sayi)#sayi 3 ün katı ise sayi yazdırır
    

#2-sayılar lıstesındekı sayıların toplamı kaçtır?
toplam=0#toplam değişkeni 0'a eşitlenir
for sayi in sayilar:
    toplam+=sayi#toplam değişkeni sayi değişkeni ile toplanır
print(toplam)#toplam değişkeni yazdırır

#3-sayılar listesındekı tek sayıların karesını alınız
for sayi in sayilar:
    if (sayi%2==1):#sayi 2'ye bölünüyor mu diye kontrol eder
        print(sayi**2)#sayi 2'ye bölünüyor ise sayi'nın karesi yazdırır


sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
#5-sehirlerden hangileri en fazla 5 karakterlidir?
for sehir in sehirler:
    if (len(sehir)>=5):#sehir'in uzunluğu 5'ten büyük mü diye kontrol eder len() fonksiyonu sehir'in uzunluğunu verir
        print(sehir)#sehir'in uzunluğu 5'ten büyük ise sehir yazdırır


urunler=[
    {"name":"samsung s6","price":3000},
    {"name":"samsung s7","price":4000},
    {"name":"samsung s8","price":5000},
    {"name":"samsung s9","price":6000},
    {"name":"samsung s10","price":7000},

]
#ürünlerin fiyatları toplamı kaçtır?
toplam=0#toplam değişkeni 0'a eşitlenir fiyatları toplamak için
for urun in urunler:
    toplam+=urun["price"]#toplam değişkeni urun'un fiyatı ile toplanır 
print(toplam)#toplam değişkeni yazdırır 

#7-ürünlerden  fiyatı en fazla 5000 olan ürünleri yazdırınız
for urun in urunler:
    if (urun["price"]<=5000):
        print(urun["name"])#urun'un adı yazdırır
        print(urun["price"])#urun'un fiyatı yazdırır
        print("--------------------------------")#urun'un adı ve fiyatı arasında bir boşluk bırakır