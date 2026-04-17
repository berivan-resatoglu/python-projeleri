#x=5
#y=10
#z=20

#x, y, z = 5, 10, 20
#x,y=y,x #x ve y değerlerini değiştirir
#x= x+5   #x+=5 #aynı işlem
#x-=5 #x=x-5 #aynı işlem
#x*=5 #x=x*5 #aynı işlem
#x/=5 #x=x/5 #aynı işlem
#x%=5 #x=x%5 #aynı işlem
#x//=5 #x=x//5 #aynı işlem
#y**=5 #y=y**5 #aynı işlem
#y+=5 #y=y+5 #aynı işlem
#y-=5 #y=y-5 #aynı işlem
#y*=5 #y=y*5 #aynı işlem
#y/=5 #y=y/5 #aynı işlem
#y%=5 #y=y%5 #aynı işlem
#y//=5 #y=y//5 #aynı işlem
#z**=5 #z=z**5 #aynı işlem
#z+=5 #z=z+5 #aynı işlem
#z-=5 #z=z-5 #aynı işlem
#z*=5 #z=z*5 #aynı işlem
#z/=5 #z=z/5 #aynı işlem
#z%=5 #z=z%5 #aynı işlem
#z//=5 #z=z//5 #aynı işlem
#y+=x+z #y=y+x+z #aynı işlem


#print(x,y,z)
values=1,2,3,4,5 
print(values) 
print(type(values))
x,y,*z = values
print(x,y,*z)#fazladan olan değer z degerıne atanır
print(x,y,z[0])#z degerının ilk elemanını yazdırır