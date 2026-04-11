# Identity operator :is yani iki değişken tam olarak aynı nesneye işaret ediyor mu diye bakar
x=y= [1 ,2,3]
z=[1,2,3,]
print(x==y)#true
print(x==z)#true
print(x is y)#true
print(x is z)#false
#example
x= [1 ,2,3]
y=[2,4]
print(x is y)#false

#membership oparator=in bir şeyin bir koleksiyonun içinde olup olmadığını kontrol eder
x = ["apple ", " banana" ]
print("banana " in x)#true
name ="berivan "
print("a "in name )
print("a " not in name )
