import random
import math

def RabinMiller(n):
    n_1 = n - 1
    s = 0
    temp = n_1
    while ((temp % 2) == 0):
        temp = temp // 2
        s = s + 1
    d = temp
    a_set = []
    for i in range(int(math.log(n))):
        a_set.append(random.randint(2, n - 1))
    for a in a_set:
        x = (a ** d) % n
        if x != 1:
            flag = 1
            for k in range(s):
                x2 = (a ** ((2 ** k) * d)) % n
                if x2 == n - 1:
                    flag = 0
                    break
            if flag == 1:
                return (False)
    return (True)


def genkey():
    while (True):
        key = random.randint(1000, 100000)
        if key % 2 == 1:
            if RabinMiller(key) == True:
                break
    return key


class DiffieHellman():
    def __init__(self):
        self.public_key1 = None
        self.public_key2 = None
        self.private_key = None
        self.shared_key = None
        self.reciving_key = None
        self.full_key = None

    def set_public_key1(self, public_key1):
        self.public_key1 = public_key1

    def set_public_key2(self, public_key2):
        self.public_key2 = public_key2

    def connection(self, second_node):
        self.public_key1 = random.randint(1000, 1000000)
        second_node.set_public_key1(self.public_key1)
        self.public_key2 = genkey()
        second_node.set_public_key2(self.public_key2)
        self.gen_private_key()
        second_node.gen_private_key()
        self.gen_shared_key()
        second_node.gen_shared_key()
        self.reciving_key = second_node.shared_key
        second_node.reciving_key = self.shared_key

    def gen_private_key(self):
        self.private_key = random.randint(100, 1000)

    def gen_shared_key(self):
        self.shared_key = (self.public_key1 ** self.private_key) % self.public_key2

    def gen_full_key(self):
        self.full_key = (self.reciving_key ** self.private_key) % self.public_key2

    def encrypt_msg(self, msg):
        encrypted_msg = ""
        key = self.full_key
        for c in msg:
            encrypted_msg += chr(ord(c) + key)
        return encrypted_msg

    def decrypt_msg(self, encrypted_msg):
        decrypted_msg = ""
        key = self.full_key
        for c in encrypted_msg:
            decrypted_msg += chr(ord(c) - key)
        return decrypted_msg