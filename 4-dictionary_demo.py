ogrencıler={
   "120":{

       "ad": "ali",
        "soyad":"yılmaz",
        "telefon":123456789,
    },
    "125":{
        "ad":"can",
        "soyad":"korkmaz",
        "telefon":123456987,
    },
    "128":{
        "ad":"berivan",
        "soyad":"resatoglu",
        "telefon":123654789,
    },   
}
ogrenciler={}
number=input("öğrenci no:")
name=input("öğrenci adı:")
surname=input("öğrenci soyismi:")
phone=input("öğrenci tel:")

ogrenciler[number]={
    "ad":name,
    "soyad":surname,
    "tel":phone
}
print(ogrenciler)
