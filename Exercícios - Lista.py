#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista1=[]

num1 = input ("Digite um numero inteiro.")

    
num2= input ("Digite outro numero inteiro.")

num3 = input ("Digite mais um numero inteiro.")

num4 = input ("Digite mais outro numero inteiro.")

num5 = input ("Digite só mais um numero inteiro. Prometo!")

lista1=[num1, num2, num3, num4, num5]
    
   
print(lista1)


# In[7]:


#name.sort() ordena  a lista
exerc2 = [ 1.5 , 65, 7.3, 4.5 , 0.96 ,45, 245112, 658, 54.6]
print(exerc2)
exerc2.sort()
print(exerc2)


# In[43]:


# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 
#name.reverse() reverte a ordem
exerc2 = [ 1.5 , 65, 7.3, 4.5 , 0.96 ,45, 245112, 658, 54.6]
exerc2.reverse()
print(exerc2)


# In[1]:


# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota1 = input("Digite a nota da primeira prova ")
nota2 = input("Digite a nota da segunda prova ")
nota3 = input("Digite a nota da terceira prova ")
nota4 = input("Digite a nota da quarta prova ")

notai1 =int(nota1)
notai2 =int(nota2)
notai3 =int(nota3)
notai4 =int(nota4)


notas= [notai1, notai2, notai3, notai4]
media = sum(notas)/len(notas)
print("Suas notas foram:")
print (notas)
print("e a sua média foi: ")
print(media)

if media >= 70:
    print("Parabéns! Você foi aprovado.")
else:
    print("Você está reprovado. Tente novamente.")


# In[40]:


#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
#Contador de letras e vogais

texto= input ("Digite uma frase ou um texto.")


vogal= 0
consoante= 0


texto = texto.lower() #converte para minúsculas

#removem espaços, linhas e símbolos de pontuação
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")

texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")


for letra in texto:
    if letra in "aeiou":
        vogal = vogal +1
    else:
        consoante= consoante +1

total= vogal+consoante

print ("O texto tem %d vogais." %vogal)
print("O Texto tem %d consoantes." %consoante)
print("O texto tem um total de %d letras." %total)


# In[57]:


#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

x = 1
par = []
impar= []
print('Digite 20 números.')
while x <= 20:
    n = int(input('Digite um número: [ %s ]: '%x))
    if n % 2 == 0:
            par.append(n)
    else:
            impar.append(n)
    x += 1
todos= par+impar
print ("Os números digitados foram:")
print(todos)
print("O números pares são:")
print(par)
print("Os números ímpares são:")
print(impar)
  


# In[16]:


#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

x = 1
listamedia =[]
acimamedia=[]
while x <= 10:
    nome= input ("Digite o nome do aluno:")
    nota1= float(input("Digite a nota1:"))
    nota2= float(input("Digite a nota2:"))
    nota3= float(input("Digite a nota3:"))
    nota4= float(input("Digite a nota4:"))
    
    media= (round(nota1+nota2+nota3+nota4)/4)
    
    listamedia.append(media)
    x += 1
    
for i in listamedia:
    if i >= 7.0:
        acimamedia.append(i)

print(listamedia)
genios= len(acimamedia)
print ("Tivemos %d aluno(s) com média igual ou acima de 7." %genios)  
    
    
    
    
    


# In[3]:


#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

x=1 
vetor=[]
soma= []
multi=[]
somaa=0
multii=1

print('Digite 5 números inteiros.')
while x <= 5:
    n = int(input('Digite um número: [ %s ]: '%x))
    
    vetor.append(n)
    soma.append(n)
    multi.append(n)
    x += 1
    
for i in soma:
    somaa =somaa + i
    
for i in multi:
    multii = multii * i
    
print(vetor)
print(somaa)
print(multii)

    


# In[5]:


#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

x=1
altura=[]
idade=[]

while x <= 5:
    a = int(input('Digite o peso [ %s ]: '%x))
    p = float(input('Digite a altura [ %s ]: '%x))
    
    altura.append(a)
    idade.append(p)
    x+= 1
    
altura.reverse()
idade.reverse()
print(altura)
print(idade)
    
    
    


# In[11]:


#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

x=1
vet=[]
print("Digite 5 números:" )
while x <= 5:
    a = int(input('Digite o %sº número: '%x))
    vet.append(a)
    
    x +=1
    
somaq=0
for i in vet:
    somaq= somaq + (i**2)
    
print("A soma dos quadrados dos números digitados é:")
print(somaq)


# In[30]:


#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

x=1
lista1=[]
lista2=[]
mista=[]

print("Digite 10 números para a primeira lista:" )

while x <= 10:
    a = int(input('Digite o %sº número: '%x))
    lista1.append(a)
    
    x +=1

print("Digite 10 números para a segunda lista:" )

y=1
while y <= 10:
    b = int(input('Digite o %sº número: '%y))
    lista2.append(b)
    
    y +=1
    

for i in range(0,10):
    l1a= lista1[i]
    l2a= lista2[i]
    mista.append(l1a)
    mista.append(l2a)
    
    i+=1
    
print("Primeira lista:")
print(lista1)
print("Segunda lista:")
print(lista2)
print("Lista mista:")
print(mista)


# In[33]:


#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


x=1
lista1=[]
lista2=[]
lista3=[]
mista=[]

print("Digite 10 números para a primeira lista:" )

while x <= 10:
    a = int(input('Digite o %sº número: '%x))
    lista1.append(a)
    
    x +=1

print("Digite 10 números para a segunda lista:" )

y=1
while y <= 10:
    b = int(input('Digite o %sº número: '%y))
    lista2.append(b)
    
    y +=1
    
print("Digite 10 números para a terceira lista:" )

z=1
while z <= 10:
    c = int(input('Digite o %sº número: '%z))
    lista3.append(c)
    
    z +=1
    

for i in range(0,10):
    l1a= lista1[i]
    l2a= lista2[i]
    l3a= lista3[i]
    mista.append(l1a)
    mista.append(l2a)
    mista.append(l3a)
    i+=1
    
print("Primeira lista:")
print(lista1)
print("Segunda lista:")
print(lista2)
print("Terceira lista:")
print(lista3)
print("Lista mista:")
print(mista)


# In[19]:


#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

x=1
aluno={} #declara dicionario
alt=[]
idade=[]
pqn=0

while x <= 5:
    a = int(input('Digite o idade [ %s ]: '%x))
    p = float(input('Digite a altura [ %s ]: '%x))
    alt.append(p)
    idade.append(a)
    aluno[a]=p #acrescentar item em dicionario
     
    x+= 1
    

media=(sum(alt)/len(alt))

for i in range(0,5):
    if idade[i] > 13 and alt[i] < media:
        pqn= pqn+1  
    

print(pqn)    
print(media)
print(aluno)


# In[23]:


#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual
#, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

regtemp={}

m1 = float(input("Digite a temperatura média do mês de Janeiro: "))
m2 = float(input("Digite a temperatura média do mês de Fevereiro: "))
m3 = float(input("Digite a temperatura média do mês de Março: "))
m4 = float(input("Digite a temperatura média do mês de Abril: "))
m5 = float(input("Digite a temperatura média do mês de Maio: "))
m6 = float(input("Digite a temperatura média do mês de Junho: "))
m7 = float(input("Digite a temperatura média do mês de Julho: "))
m8 = float(input("Digite a temperatura média do mês de Agosto: "))
m9 = float(input("Digite a temperatura média do mês de Setembro: "))
m10 = float(input("Digite a temperatura média do mês de Outubro: "))
m11 = float(input("Digite a temperatura média do mês de Novembro: "))
m12= float(input("Digite a temperatura média do mês de Dezembro: "))

regtemp["Janeiro"]=m1
regtemp["Fevereiro"]=m2
regtemp["Março"]=m3
regtemp["Abril"]=m4
regtemp["Maio"]=m5
regtemp["Junho"]=m6
regtemp["Julho"]=m7
regtemp["Agosto"]=m8
regtemp["Setembro"]=m9
regtemp["Outubro"]=m10
regtemp["Novembro"]=m11
regtemp["Dezembro"]=m12



temp=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]

media = round(sum(temp)/len(temp))
mediano=[]

a=0
regtemp
print("A temperatura média anual é: %d ºC" %media)
i=0


#Como que puxa a key do dicionário por variável??


# In[31]:


#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

p1 = (input("Telefonou para a vítima? sim ou não "))
p2 = (input("Esteve no local do crime? sim ou não "))
p3 = (input("Mora perto da vítima? sim ou não " ))
p4 = (input("Devia para a vítima? sim ou não "))
p5 = (input("Já trabalhou com a vítima? sim ou não " ))

resposta =[p1, p2, p3, p4, p5]
a= 0
for i in resposta:
    if i == "sim":
        a= a+1


if a == 2:
    print("Classificação: SUSPEITO!")
elif a== 3 or a==4:
    print("Classificação: CÚMPLICE!")
elif a== 5:
    print("Classificação: ASSASSINO!")
elif a== 1 or a==0:
    print("Classificação: INOCENTE!")


# In[27]:


#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#ordene a lista
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

a=[]
add=[]
notas=[]
     
n = int(input("Digite a nota dos alunos:"))
while n != -1:
    n = int(input("Digite a nota dos alunos:"))
    add.append(n)

for i in add:
    if i !=-1:
        notas.append(i)
i+= 1
      
print("O total de notas digitadas foram:")
print(len(notas))
print("As notas digitadas foram:")
print(notas)

notas.reverse()
print(" A lista inversa é:")
print(notas)

notas.sort()
print(" A lista ordenada é:")
print(notas)

c= sum(notas)
print("A soma das notas é: %d" %c)

media= sum(notas)/len(notas)
print("A média das notas é: %d " %media)

acima=0
abaixo=0
for x in notas:
        if x< 7:
            acima = acima + 1
        elif x>=7:
            abaixo= abaixo+1
x+= 1
       
print("Temos %d notas acima da média." %acima)
print("Temos %d notas abaixo da média." %abaixo)


# In[15]:


#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
#Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, 
#um total de $470. Escreva um programa (usando um array de contadores) que 
#determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299   H
#$300 - $399   G
#$400 - $499   F
#$500 - $599   E
#$600 - $699   D
#$700 - $799   C
#$800 - $899  B
#$900 - $999  A
#$1000 em diante

com=0
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
top=[]


v= int(input("Digite o número de vendedores:"))

for i in range (0,v):
    venda = int(input("Digite a as vendas da semana:"))
    com= (200 + venda*0.09)
    
    if com >= 200 and com<=299:
        h.append(com)    
    elif com >= 300 and com <=399:
        g.append(com)
    elif com >= 400 and com <=499:
        f.append(com)
    elif com >= 500 and com<=599:
        e.append(com)
    elif com >= 600 and com<=699:
        d.append(com)
    elif com >= 700 and com <=799:
        c.append(com)
    elif com >= 800 and com <=899:
        b.append(com)
    elif com >= 900 and com <=999:
        a.append(com)
    elif com >= 1000:
        top.append(com)
        
linha=["top", "a", "b", "c", "d", "e", 'f', "g", 'h']

print("Vendedores nível Top: %s" %len(top))

print("Vendedores nível A: %s" %len(a))


print("Vendedores nível B: %s" %len(b))


print("Vendedores nível C: %s" %len(c))


print("Vendedores nível D: %s" %len(d))


print("Vendedores nível E: %s" %len(e))


print("Vendedores nível F: %s" %len(f))


print("Vendedores nível G: %s" %len(g))


print("Vendedores nível H: %s" %len(h))


# In[ ]:


#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
#O resultado do atleta será determinado pela média dos cinco valores restantes. 
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o 
#nome, os saltos e a média dos saltos. 
#O programa deve ser encerrado quando não for informado o nome do atleta. 
#A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

arq={}
notas=[]
nome=""
while True:
    nome= str(input("Digite o nome do atleta:"))
    if nome != "":
        at=nome
        salto1= float(input("Digite a primeira nota:"))
        salto2= float(input("Digite a segunda nota:"))
        salto3= float(input("Digite a terceira nota:"))
        salto4= float(input("Digite a quarta nota:"))
        salto5= float(input("Digite a quinta nota:"))
        notas.append(salto1)
        notas.append(salto2)
        notas.append(salto3)
        notas.append(salto4)
        notas.append(salto5)
        arq[at]=notas
        media=sum(notas)/len(notas)
        print("Resumo:")
        print("Atleta: %s" %at)
        print("Primeiro salto: %s m" %salto1)
        print("Segundo salto: %s m" %salto2)
        print("Terceiro salto: %s m" %salto3)
        print("Quarto salto: %s m" %salto4)
        print("Quinto salto: %s m" %salto5)
        print("Resultado final: ")
        print("Atleta: %s" %at)
        print( "Saltos: %s - %s - %s - %s - %s " %(salto1,salto2, salto3, salto4, salto5))#inserir notas
        print("Média dos saltos: %s m" %media)
        
    else:
            break


# In[ ]:


jog1=0
jog2=0
jog3=0
jog4=0
jog5=0
jog6=0
jog7=0
jog8=0
jog9=0
jog10=0
jog11=0
jog12=0
jog13=0
jog14=0
jog15=0
jog16=0
jog17=0
jog18=0
jog19=0
jog20=0
jog21=0
jog22=0
jog23=0
lista=[jog1,jog2,jog3,jog4,jog5,jog6,jog7,jog8,jog9,jog10,jog11,jog12,jog13,jog14,jog15,jog16,jog17,jog18,jog19,jog20,jog21,jog22,jog23]

while True:
    voto= int(input("Quem foi o melhor jogador? (Digite o número da camisa) :"))
    
    if voto == 1:
        jog1= jog1+1
    elif voto == 2:
        jog2= jog2+1
    elif voto == 3:
        jog3= jog2+1    
    elif voto == 4:
        jog4= jog4+1
    elif voto == 5:
        jog5= jog5+1
    elif voto == 6:
        jog6= jog6+1
    elif voto == 7:
        jog7= jog7+1
    elif voto == 8:
        jog8= jog8+1    
    elif voto == 9:
        jog9= jog9+1
    elif voto == 10:
        jog10= jog10+1
    elif voto == 11:
        jog11= jog11+1
    elif voto == 12:
        jog12= jog12+1    
    elif voto == 13:
        jog13= jog13+1
    elif voto == 14:
        jog14= jog14+1
    elif voto == 15:
        jog15= jog15+1
    elif voto == 16:
        jog16= jog16+1
    elif voto == 17:
        jog17= jog17+1
    elif voto == 18:
        jog18= jog18+1    
    elif voto == 19:
        jog19= jog19+1
    elif voto == 20:
        jog20= jog20+1
    elif voto == 21:
        jog21= jog21+1
    elif voto == 22:
        jog22= jog22+11
        
    elif voto == 23:
        jog23= jog23+1 
    elif voto == 0:
        break
    else:
       voto=input("Jogador inválido. Digite um número de 1 a 23 ou 0 para finalizar: ")
  
total=(jog1+jog2+jog3+jog4+jog5+jog6+jog7+jog8+jog9+jog10+jog11+jog12+jog14+jog13+jog15+jog16+jog17+jog18+jog19+jog20+jog21+jog22+jog23)
lista=[jog1,jog2,jog3,jog4,jog5,jog6,jog7,jog8,jog9,jog10,jog11,jog12,jog13,jog14,jog15,jog16,jog17,jog18,jog19,jog20,jog21,jog22,jog23]

print("Tivemos um total de %s votos." %total)


tx1= round(jog1*100/total)
tx2= round(jog2*100/total)
tx3= round(jog3*100/total)
tx4= round(jog4*100/total)
tx5= round(jog5*100/total)
tx6= round(jog6*100/total)
tx7= round(jog7*100/total)
tx8= round(jog8*100/total)
tx9= round(jog9*100/total)
tx10= round(jog10*100/total)
tx11= round(jog11*100/total)
tx12= round(jog12*100/total)
tx13= round(jog13*100/total)
tx14= round(jog14*100/total)
tx15= round(jog15*100/total)
tx16= round(jog16*100/total)
tx17= round(jog17*100/total)
tx18= round(jog18*100/total)
tx19= round(jog19*100/total)
tx20= round(jog20*100/total)
tx21= round(jog21*100/total)
tx22= round(jog22*100/total)
tx23= round(jog23*100/total)

print(" Jogador    -   Votos    -   %")
if jog1>0:
     print( "    1             %s         %s%% " %(jog1,tx1))
if jog2>0:
     print( "    2             %s         %s%% " %(jog2,tx2))
if jog3>0:
     print( "    3             %s         %s%% " %(jog3,tx3))
if jog4>0:
     print( "    4             %s         %s%% " %(jog4,tx4))
if jog5>0:
     print( "    5             %s         %s%% " %(jog5,tx5))
if jog6>0:
     print( "    6             %s         %s%% " %(jog6,tx6))
if jog7>0:
     print( "    7             %s         %s%% " %(jog7,tx7))
if jog8>0:
     print( "    8             %s         %s%% " %(jog8,tx8))
if jog9>0:
     print( "    9             %s         %s%% " %(jog9,tx9))
if jog10>0:
     print( "   10             %s         %s%% " %(jog10,tx10))
if jog11>0:
     print( "   11             %s         %s%% " %(jog11,tx11))
if jog12>0:
     print( "   12             %s         %s%% " %(jog12,tx12))
if jog13>0:
     print( "   13             %s         %s%% " %(jog13,tx13))
if jog14>0:
     print( "   14             %s         %s%% " %(jog14,tx14))
if jog15>0:
     print( "   15             %s         %s%% " %(jog15,tx15))
if jog16>0:
     print( "   16             %s         %s%% " %(jog16,tx16))
if jog17>0:
     print( "   17             %s         %s%% " %(jog17,tx17))
if jog18>0:
     print( "   18             %s         %s%% " %(jog18,tx18))
if jog19>0:
     print( "   19             %s         %s%% " %(jog19,tx19))
if jog20>0:
     print( "   20             %s         %s%% " %(jog20,tx21))
if jog21>0:
     print( "   21             %s         %s%% " %(jog21,tx21))
if jog22>0:
     print( "   22             %s         %s%% " %(jog22,tx22))
if jog23>0:    
     print( "   23            %s         %s%% " %(jog23,tx23))


tp=max(lista)
tpp=round(tp*100/total)
i=0
for i in range(0,23):
     if lista[i] == tp:   
         mais=i
    
g=mais+1

print("O jogador mais votado foi o camisa %s com %s votos, correspondendo a %s%% do total de votos." %(g,tp,tpp))


# In[ ]:


print("Na enquete: Qual o melhor Sistema Operacional para uso em servidores?")

so1= int(input("Quantos votos o SO1- Windows Server recebeu? :"))
so2= int(input("Quantos votos o SO2- Unix recebeu? :"))
so3= int(input("Quantos votos o SO3- Linux recebeu? :"))
so4= int(input("Quantos votos o SO4- Netware recebeu? :"))
so5= int(input("Quantos votos o SO5- Mac OS recebeu? :"))
so6= int(input("Quantos votos a opção 6- Outros recebeu? :"))

votos=[so1,so2,so3,so4,so5,so6]
sos=["Windows Server","Unix","Linux","Netware","Mac OS","Outros"]
total=sum(votos)

po1=round(so1*100/total)
po2=round(so2*100/total)
po3=round(so3*100/total)
po4=round(so4*100/total)
po5=round(so5*100/total)
po6=round(so6*100/total)

tp=max(votos)
i=0
for i in range(0,6):
     if votos[i] == tp:   
         mais=i

melhor=mais+1
melhorp=round(tp*100/total)
melhoros=sos[mais]

print(" Sistema operacional       votos    %")
print(" -------------------       -----    ---")
print("1- Windows Server           %s     %s"%(so1,po1))
print("2- Unix                     %s     %s"%(so2,po2))
print("3- Linux                    %s     %s"%(so3,po3))
print("4- Netware                  %s     %s"%(so4,po4))
print("5- Mac OS                   %s     %s"%(so5,po5))
print("6- Outros                   %s     %s"%(so6,po6))
print("O Sistema Operacional mais votado foi o %s, com %s votos, correspondendo a %s%% dos votos." %(melhoros,tp,melhorp))


# In[ ]:


#O salário de cada funcionário, juntamente com o valor do abono;
#O número total de funcionário processados;
#O valor total a ser gasto com o pagamento do abono;
#O número de funcionário que receberá o valor mínimo de 100 reais;
#O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

n=int(input("Digite a quantidade de funcionários a calcular:"))
salario=[]
abono=[]
salab={}
vab=0
t=0
y=0
for i in range(0,n):
    sal=int(input("Digite o salário do funcionário [%s]: " %i))
    salario.append(sal)

for y in salario:
        vab= round(y*0.2)
        if vab > 200 :
            abono.append(vab)
        else:
            t=t+1
            abono.append(100)
            
i+=1
total=sum(abono)
maior=max(abono)

print("Projeção de gastos com abono")
print("------------------------------")
for x in salario:
     
    print(" Salário = %s" %x)

print("Salário:        Abono:    ")
for i in range(0,n):
  
      print("R$ %s    -    R$ %s    "%(salario[i],abono[i]))

print("Foram cadastrados %s colaboradores." %n)
print("Total gasto com abono: R$ %s" %total)
print("Valor mínimo pago a %s colaboradores" %t)
print("Maior valor de abono: R$ %s" %maior)


# In[1]:


#cadastrar 5 veículos com seu consumo sair o carro mais economic
# Quantos litros de combustível cada um dos carros cadastrados consome para 
#percorrer uma distância de 1000 quilômetros e quanto isto custará, 
#considerando um que a gasolina custe R$ 2,25 o litro.

carros=[]
kmsh=[]
consumor=[]
consumol=[]

for i in range(1,6):
    carro= input("Digite o modelo do carro %d: " %i)
    kmh= float(input("Digite o consumo médio do carro %d: " %i))
    consr=(1000/kmh*2.25)
    consl=(1000/kmh)
    carros.append(carro)
    kmsh.append(kmh)
    consumor.append(consr)
    consumol.append(consl)
    
z=kmsh.index(max(kmsh))
t=carros[z]


for x in range(0,5):
    y=x+1
    c=carros[x]
    d=kmsh[x]

    print("Veículo %d" %y)
    print("Modelo: %s" %c)
    print("Consumo %d km/l" %d)
    print("-------------------------------------------")

print( "Relatório final: ")
for g in range(0,5):
    h=g+1
    i=carros[g]
    j=kmsh[g]
    r=consumor[g]
    l=consumol[g]
    print("%d - %s - %d km/l   - %d litros - R$ %d   "%(h,i,j,l,r))

print("O modelo mais econômico é o %s." %t)


# In[1]:


def1=0
def2=0
def3=0
def4=0


print("Bem vindo ao cadastro de sucatas!")
print("Para os cadastros dos mouses danificados, escolha um dos defeitos na lista abaixo:")
print("1 - Necessita de esferas")
print("2 - Necessita de limpeza")
print("3 - Necessita troca do cabo ou conector")
print("4 - Quebrado ou inutilizado ")

while True:     
     defeito=int(input("Digite o defeito encontrado ou 0 para encerrar: "))
     if defeito == 1:
       def1=def1+1
     elif defeito == 2:
       def2=def2+1
     elif defeito == 3:
       def3=def3+1
     elif defeito == 4:
       def4=def4+1
     elif defeito == 0:
       break
     else:
         defeito=int(input("Numero inválido. Digite o defeito de 1 a 4 ou 0 para encerrar:  "))
total= def1+def2+def3+def4
def1p= round(def1*100/total)
def2p= round(def2*100/total)
def3p= round(def3*100/total)
def4p= round(def4*100/total)


print("--------------------------------------------------------------------------")
print("---------------- Quantidade de mouses: %d  -------------------------------" %total)
print("--------------------------------------------------------------------------")
print("Situação                             Quantidade              Percentual ")
print("--------------------------------------------------------------------------")
print("1 - Necessita de esferas                  %s          %s%%" %(def1,def1p) )
print("2 - Necessita de limpeza                  %s          %s%%" %(def2,def2p) )
print("3 - Necessita troca do cabo ou conector   %s          %s%%" %(def3,def3p) )
print("4 - Quebrado ou inutilizado               %s          %s%%" %(def4,def4p) )


# In[ ]:




