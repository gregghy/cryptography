#riesce a codificare e decodificare anche frasi con degli spazi e maiuscole, ma solo se non e la A ad essere maiscuola, altrimenti esce errore visto che la A in bin e 1000001 e gli spazi sono 100000, ed il programma cerca per identificare gli spazi sequenze di 0 pari a 5
#the program will not compile if the input phrase has the capitol A or interpunction (,.!?' ecc)
import math
def encode(text):
    l,m=[],[]
    binary = ""
    result = 0
    
    for i in text:
        l.append(ord(i))
    
    for i in l:
        m.append(int(bin(i)[2:]))
    
    for i in m:
        binary = binary + str(i)

    result = int(binary, 2)

    print("la frase cifrata: " + str(result))
    return result

        
def decode(number):
    binary = str(bin(number)) 
    binary = binary[2:]

    l = []
    
    counter = 0
    number = ""
    zeri = 0
    
    #divide il codice binario nelle varie lettere
    for i in binary:
        number = number + i
        counter = counter + 1
        if i == '0':
            zeri = zeri + 1
        if zeri > 4:
            l.append(number)
            number = ""
            counter = 0
            zeri = 0
        if counter > 6:
            l.append(number)
            number = ""
            counter = 0
            zeri = 0

    #cambia il codice binario delle lettere in int
    n = []
    
    for i in l:
        n.append(int(i))
    
    #converte il codice binario in lettere
    q=[]
    m=""
    for i in n:
        b=0
        c=0
        k=int(math.log10(i))+1
        for j in range(k):
            b=((i%10)*(2**j))   
            i=i//10
            c=c+b
        q.append(c)
    for x in q:
        m=m+chr(x)

    print("La frase decifrata: " + m)

decode(encode(""))
