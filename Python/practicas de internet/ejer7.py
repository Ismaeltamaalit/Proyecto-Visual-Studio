#str_x = "Emma is good developer. Emma is a writer"
str_x = input("Escribe una frase")

print(str_x)

palabra=input("escribe una palabra que esté dentro de la frase que has escrito, para comprobar cuanto aparece")

# use count method of a str class
cnt = str_x.count(palabra)
if cnt==0:
    print("escribe una palabra dentro de tu propia frase")
else:
    print(cnt)
