frsone = "Why so serious ?" 
print ("String 1:",frsone) 
frstwo = "Run Florest, Run"
nuone = len(frsone)
nutwo = len(frstwo)
t = "Tamanho de '%s' é {}" % (frsone)
x = "Tamanho de '%s' é {}" % (frstwo)
print ("String 2:", frstwo) 
print (t.format (nuone))
print (x.format(nutwo))
if (len(frsone) != len(frstwo)):
    print ("As duas strings são de tamanhos diferentes")
else :
 print("As duas strings são iguais") 

if frsone == frstwo:
    print('Iguais')
else:
    print('Diferente')
if (x == True):
    print("As duas strings possuem conteúdo iguais")
else:
    print("As duas strings possuem conteúdo diferente")





   
  