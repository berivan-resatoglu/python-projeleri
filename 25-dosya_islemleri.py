import json#json modülünü import eder
with open("data.json" , "r" , encoding="utf-8") as file: #dosyayı okur ve json formatına çevirir
    data=json.load(file)#dosyayı okur ve json formatına çevirir

with open("data.json" , "w" , encoding="utf-8") as file:#dosyayı yazılır ve json formatına çevirir
     kitapadi=input("kitap adını giriniz:")#kitap adını giriniz
     yazar=input("yazarını giriniz:")#yazarını giriniz
     fiyat=input("fiyatını giriniz:")#fiyatını giriniz
     yayin_yili=input("yayın yılını giriniz:")#yayın yılını giriniz
     yayıncılık=input("yayıncılıkını giriniz:")#yayıncılıkını giriniz
     kategori=input("kategoriyı giriniz:")#kategoriyı giriniz
     müsait=bool(input("müsait mi? (e/h):"))#müsait mi?
     data.append(
        {
            "kitapadi":kitapadi,#kitap adı
            "yazar":yazar,#yazar
            "fiyat":fiyat,#fiyat
            "yayin_yili":yayin_yili,#yayın yılı
            "yayıncılık":yayıncılık,#yayıncılık
            "kategori":kategori,#kategori
            "müsait":müsait,#müsait mi?

        }
     )
     json.dump(data,file,indent=4, ensure_ascii=False)#dosyayı yazılır ve json formatına çevirir



