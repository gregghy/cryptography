def algoritmo_euclide(a, b):
    # a - b*q = r
    A = []
    while b > 0:
        r = a % b 
        n = a/b - r/b

        a = b
        b = r
        
        A.append(n)
        #per aver l'MCD fare return a, per avere la lista fare return A
        #GCD is a, the list of quotients
    return a, A
#insert the biggest number of the two as a (the first one)
print(algoritmo_euclide(26, 11))

def bezout(list):
    list = list[:-1]
    
    x = list[-1]
    y = -list[-1]
    
    while len(list) > 1:
        list.pop(len(list)-1)
        t = x
        x = y
        y = t - y * list[-1]
    return x, y


print(bezout(algoritmo_euclide(1814, 1567)[1]))

def matr(M):
    a = M[0][0]
    b = M[0][1]
    c = M[1][0]
    d = M[1][1]
    det = a * d - c * b
    
    if algoritmo_euclide(26, det)[0] != 1:
        return False
    return True
print(matr([[1, 1],[4, 6]]))

def encode_Hill(text, M):
    if matr(M) != True:
        return "La matrice indicata non va bene"
    
    diz1 = {'Z':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25}
    diz2 = {0:'Z', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y'}
    
    val1 = diz1[text[:1]]
    val2 = diz1[text[1:]]
    
    
    v = [[val1],[val2]]
    w = [M[0][0]*v[0][0] + M[0][1]*v[1][0], M[1][0]*v[0][0] + M[1][1]*v[1][0]]

    w[0] = w[0] % 26

    w[1] = w[1] % 26

    result = diz2[w[0]] + diz2[w[1]]
    
    return result
   
print(encode_Hill('AY', [[5, 1],[5, 4]]))

def decode_Hill(text, M):
    if matr(M) != True:
        return "La matrice indicata non va bene"
    
    a = M[0][0]
    b = M[0][1]
    c = M[1][0]
    d = M[1][1]
    det = a * d - c * b
    x = bezout(algoritmo_euclide(26, det)[1])[0]
    y = bezout(algoritmo_euclide(26, det)[1])[1]
    
    diz1 = {'Z':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25}
    diz2 = {0:'Z', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y'}
    
    val1 = diz1[text[:1]]
    val2 = diz1[text[1:]]
    
    v = [[val1],[val2]]
    
    
    M1 = [[d, -b],[-c, a]]
    
    w = [M1[0][0]*v[0][0] + M1[0][1]*v[1][0], M1[1][0]*v[0][0] + M1[1][1]*v[1][0]]
    
    w[0] = w[0] * y
    w[1] = w[1] * y
    
    w[0] = w[0] % 26
        
    w[1] = w[1] % 26
        
    result = diz2[w[0]] + diz2[w[1]]
    
    return result
print(decode_Hill(encode_Hill('AY', [[5, 1],[5, 4]]), [[5, 1],[5, 4]]))

#text only in capitol letters and spaces
def text_encode(text, M):
    #divide spazi da lettere e poi le lettere in coppie
    A = []
    b =""

    index = 0

    for i in text:
        if i == " " or i ==',' or i == "." or i == ":" or i == ";":
            A.append(index)
        else:
            b = b + i

        index = index + 1

    C = []
    for i in range(0, len(b), 2):
        C.append(b[i: i + 2])

    print(A)
    #codifica lettere
    result = ""

    for i in C:
        result = result + encode_Hill(i, M)


    return result
    
print(text_encode("HELLO WORLD", [[5, 1],[5, 4]]))

def text_decode(text, M):
    #dividere il test in sillabe
    A = []
    for i in range(0, len(text), 2):
        A.append(text[i: i + 2])
    
    #decodifica lettere
    result = ""

    for i in A:
        result= result + decode_Hill(i, M)
    

    return result

print(text_decode(text_encode("HELLO WORLD", [[5, 1],[5, 4]]), [[5, 1],[5, 4]]))



