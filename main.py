from DiffieHellman import DiffieHellman

if __name__ == '__main__':
    bob = DiffieHellman()
    alice = DiffieHellman()
    bob.connection(alice)
    bob.gen_full_key()
    alice.gen_full_key()
    message = alice.encrypt_msg("Hello! My name is Alice")
    print(message)
    print(bob.decrypt_msg(message))