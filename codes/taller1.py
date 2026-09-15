import random

def union(a, b):
    c = set()
    for elemento in a:
        c.add(elemento)
    for elemento in b:
        c.add(elemento)
    return c

def interseccion(a, b):
    c = set()
    for elemento in a:
        if elemento in b:
            c.add(elemento)
    return c

def diferencia(a,b):
    c = set()
    for elemento in a:
        if elemento not in b:
            c.add(elemento)
        return c

def diferencia_simetrica(a,b):
    d1 = diferencia(a,b)
    d2 = diferencia(b,a)
    return union(d1,d2)

A = set()
ca = 10
while len(A) < ca:
    numero = random.randint(0, 30)
    A.add(numero)

B = set()
while len(B) < ca:
    numero = random.randint(0, 30)
    B.add(numero)

print(f'A = {A}')
print(f'B = {B}')
N = union(A,B)
M = interseccion(A, B)
G = diferencia(A, B)
R = diferencia (B, A)
D = diferencia_simetrica(A,B)
print(f'union: {N}')
print(f'interseccion: {M}')
print(f'diferencia A-B: {G}')
print(f'diferencia B-A: {R}')
print(f'diferencia simetrica: {D}')
        
