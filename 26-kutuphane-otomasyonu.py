import json#json modülünü import eder
with open("data.json" , "r", encoding="utf-8") as file:#dosyayı okur ve json formatına çevirir
    data=json.load(file)#dosyayı okur ve json formatına çevirir

while True:#sonsuz döngü
    print(""" 
    (1) kitap ekle
    (2) kitap sil
    (3) kitap vermek
    (4) kitap listele
    (5) çıkış
    """)
    
    secim=input("seçiminizi yapınız:")#seçimi yapınız
    if secim=="1":#seçim 1 ise kitap ekle
        with open("data.json" , "w" , encoding="utf-8") as file:#dosyayı yazılır ve json formatına çevirir
            kitapadi=input("kitap adını giriniz:")#kitap adını giriniz
            yazar=input("yazarını giriniz:")#yazarını giriniz
            fiyat=int(input("fiyatını giriniz:"))#fiyatını giriniz
            yayın_yili=input("yayın yılını giriniz:")#yayın yılını giriniz
            yayıncılık=input("yayıncılıkını giriniz:")#yayıncılıkını giriniz
            kategori=input("kategoriyi giriniz:")#kategoriyi giriniz
            müsaitlik=bool(input("müsait mi? (e/h):"))#müsait mi?
            data.append({
                

                "kitapadi":kitapadi,#kitap adı
                "yazar":yazar,#yazar
                "fiyat":fiyat,#fiyat
                "yayın_yili":yayın_yili,#yayın yılı
                "yayıncılık":yayıncılık,#yayıncılık
                "kategori":kategori,#kategori
                "müsait":müsaitlik,#müsait mi?
                
            })
            json.dump(data,file,indent=4, ensure_ascii=False)#dosyayı yazılır ve json formatına çevirir


    elif secim=="2":#seçim 2 ise kitap sil

        with open("data.json" , "w" , encoding="utf-8") as file:#dosyayı yazılır ve json formatına çevirir
            kitapadi=input("silinecek kitap adını giriniz:")#silinecek kitap adını giriniz
            for kitap in data:#kitap adını sil
                if kitap["kitapadi"]==kitapadi:#kitap adı eşleşiyorsa kitap sil
                    data.remove(kitap)#kitap sil
                    break
                else:
                    print("kitap bulunamadı")
            json.dump(data,file,indent=4, ensure_ascii=False)#dosyayı yazılır ve json formatına çevirir

    elif secim=="3":
        with open("data.json","w",encoding="utf-8") as file:
            kitapadi=input("verilecek kitap adını giriniz:")

        bulundu=False

        for kitap in data:
            if kitap["kitapadi"]==kitapadi:
                kitap["müsait"]=True
                bulundu=True
                break

        if not bulundu:
            print("kitap bulunamadı")

        json.dump(data,file,indent=4,ensure_ascii=False)




    elif secim=="4":#seçim 4 ise kitap sil

        for kitap in data:#kitap adını listele  

            print("-"*50)
            print("kitap adı:",kitap["kitapadi"])
            print("yazar:",kitap["yazar"])
            if kitap["müsait"]:

                print("müsait:",kitap["müsait"])
            else:
                print("müsaitlik:hayır")
            print("-"*50)

    elif secim=="5":#seçim 5 ise çıkış
        print("GÖRÜŞÜRÜZZZ KENDİNE CİCİ BAK 😘😘😘")
        break

    




