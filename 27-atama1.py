x,y,z=2,5,10
numbers=1,5,7,10,6

#1-kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamını  farkı nedir
a=int(input("1. sayı:"))
b=int(input("2. sayı:"))
result=(a*b)-(x+y+z)
print(result)
#2-y'nin x'e kalansız bölümünü hesaplayınız
result=y//x



#3-(x,y,z) toplamın mod 3'ü nedir
toplam=(x+y+z)
result=toplam%3
#4-y'nin x. kuvvetini hesaplayınız
result=y**x

#5- x, *y, z = numbers işlemine göre z nin küpü kaçtır
numbers=(1,5,7,10,6)
x, *y, z = numbers 
result=z**3
#6- x, *y, z = numbers işlemine göre y'nin değerler toplamı  kaçtır
numbers=(1,5,7,10,6)
x, *y, z = numbers 
result=y[0]+y[1]+y[2]
print(result)