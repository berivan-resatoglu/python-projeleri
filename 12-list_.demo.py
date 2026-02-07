#1-"bmw","mercedes","opel","mazda" elemanlarını içeren bir liste oluşturunuz.
arabalar=["bmw","mercedes","opel","mazda"] 

#2-liste kaç elemanlıdır?
result=len(arabalar)
# 3-listenin ilk ve son elemanını yazdırınız.
print(arabalar[0])
print(arabalar[3])
#4-mazda değerini toyota ile değiştiriniz.
arabalar[-1]="toyota"
print(arabalar)
#5-mercedes listenin bir elemanı mıdır?
result= "mercedes" in arabalar#in operatörü liste içinde aranan değer var mı diye kontrol eder
#13.kod satırında neden print yazmadık?
#terminali çaliştırdığımız zaman tüm kodlar çalışıyor ama hocanın çalışmadı
#6-listenin -2 indeksinin değerini yazdırınız.
result=arabalar[-2]
#listenin ilk 3 elemanını yazdırınız.
result=arabalar[0:3]
result=arabalar[:3]
result=arabalar[-2:]
#8-listenin son 2 elemanının yerine "toyota" ve "renault" değerlerini ekleyiniz.
arabalar[-2:]=["toyota","renault"]
result=arabalar
#9-listenin üzerine "ford" ve "audi" değerlerini ekleyiniz.
result=arabalar + ["ford","audi"]
print(result)
#listenin son elemanını siliniz.
del arabalar[-2]#burda çalışmadı 
result=arabalar
#10-liste elemanlarını tersten yazdırınız.
result=arabalar[::-1]#burda da çalışmadı :(
#aşağıdaki verileri bir liste içinde saklayınız 
#studentA: yigit bilgi 2010 ,(70,60,70)
#studentB:sena turan :1998,(80,80,70)
#studentC:ahmet turan :1998,(80,70,90
studentA=["yigit" , "bilgi" ,2010 ,(70,60,70)]
studentB=["sena" ,"turan" ,1998,(80,80,70)]
studentC=["ahmet" , "turan" ,1998,(80,70,90)]
result=studentA[0]

