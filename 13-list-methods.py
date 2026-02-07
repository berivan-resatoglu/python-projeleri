numbers=[1, 2, 10, 15,16]
letters=["a", "b", "g", "a", "g"]
val=min(numbers)
val=max(numbers)
val=max(letters)#alfebatik olarak sıralar
#print(val)
val=numbers[3:5]
val=numbers[:3]
#print(val)
numbers[3]=40
numbers.append(49)#parantez içine alınan sayıyı ekler
numbers.insert(3, 78)
numbers.insert(-1, 1956324)#ekleme yapar
numbers.pop(0)#0.elemanını siler
numbers.remove(49)#parantez içine alınan sayıyı kaldırır
print(numbers)
numbers.sort()#sort sıralama yapar sayılarda küçükten büyüğe,harflerde ise alfabetik sıralamaya göre yapar
letters.sort()
numbers.reverse()#sort un tersini yapar
print(numbers)
print(letters)
print(len(numbers))#eleman sayısını hesaplar
print(numbers.count(10))#parantez içine alınan sayıdan kaç tane olduğunu gösterir
numbers.clear()#numbers teki tüm elemanları siler
print(numbers)