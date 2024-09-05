lista = [1, 4, 6, 7, 13, 9, 67]
primos = []

def es_primo(n):

    if n <= 1:
        return False
    elif n == 2: 
        return True
    else: 
        for i in range(2,n): 
            if n % i == 0:
                return False
        return True
    

def nueva_lista():
    for numero in lista: 
        if es_primo(numero):
            primos.append(numero)
    print(primos)


nueva_lista()