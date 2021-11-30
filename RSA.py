from sympy import isprime
from random import randint


class Person:
    e = 0
    n = 0
    d = 0
    m = 0
    c = 0

    def __init__(self, e1, n1, d1):
        self.e = e1
        self.n = n1
        self.d = d1

    def decrypt(self, c):
        self.m = (c**self.d) % self.n
        return self.m

    def encrypt(self, mess):
        self.c = (mess**self.e) % self.n
        return self.c


while True:
    p = randint(1000, 10000)
    if isprime(p):
        break
while True:
    q = randint(1000, 10000)
    if isprime(q):
        break
n = p*q
fin = (p-1)*(q-1)
while True:
    e = randint(3, 10000000)
    if isprime(e) and e<fin:
        break
d = 445
while not (d*e) % fin==1:
    d+=1
Masha = Person(e, n, d)
Pasha = Person(e, n, d)
m = Masha.encrypt(1111)
print("Зашифрованное сообщение =", m)
p = Pasha.decrypt(m)
print("Расшифрованное сообщение =", p)
