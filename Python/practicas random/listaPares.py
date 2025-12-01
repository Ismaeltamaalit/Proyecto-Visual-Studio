lista=[]
num=int(input("introduce un numero"))
for i in range(1,num+1):
    if i % 2 ==0:
        lista.append(i)
print(lista)