fruits={"orange","apple","banana"}
print(fruits)
#print(fruits[0])#setlerde indexleme yapılamaz

for x in fruits:
    print(x)
fruits.add("cherry")
print(fruits)
fruits.update(["mango","pineapple"])
print(fruits)
fruits.update(["cherry","mango","pineapple","apple"])
print(fruits)#setlerde tekrar eden elemanlar otomatik olarak silinir
mylist=[1,2,3,4,4,5,1,]
print(mylist)
#mylist=[1,2,3,4,4,5,1,]
#mylist=set(mylist)
#print(mylist)#tekrar eden elemanları tekrar ederek yazdırır

fruits.remove("apple")#setlerde eleman silmek için remove kullanılır
print(fruits)

fruits.discard("banana")#setlerde eleman silmek için discard kullanılır
print(fruits)
 
 