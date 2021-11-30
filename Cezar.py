def cezar(encrypt, key1):  # Функция простого шифра Цезаря
    alphabet3 = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
    encrypt = encrypt.lower()
    encrypted = ''
    for super in encrypt:
        if super in alphabet3:
            pos = alphabet3.find(super)
            new_pos = pos + (key1 % 32)
            encrypted += alphabet3[new_pos]
        else:
            encrypted += super
    return encrypted


def new_alphabet(key_word, key_at_alp):  # Функция для генерации алфавита с ключевым словом
    alphabet2 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    new_alpha = ''
    key_word = key_word.lower()
    for sleep in alphabet2:
        if sleep not in key_word:
            new_alpha += sleep
    alphabet2 = ''
    alphabet2 += key_word + new_alpha
    start_alpha = alphabet2
    alphabet2 = list(alphabet2)
    for alpha in range(len(alphabet2)):
        alphabet2[(alpha + key_at_alp) % 32] = start_alpha[alpha]
    return ''.join(alphabet2)


def cezar_with_key(encrypt, key1, key_word):  # Функция шифра Цезаря с ключевым словом
    alphabet1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    second_alphabet = new_alphabet(key_word, key1)
    encrypt = encrypt.lower()
    encrypted = ''
    for symbols in encrypt:
        if symbols in alphabet1:
            pos = alphabet1.find(symbols)
            encrypted += second_alphabet[pos]
        else:
            encrypted += symbols
    return encrypted


def periods(d):  # Функция для определения частоты встречающихся символов
    max1 = 0
    max_value = 0
    period = []
    for i in range(8):
        for kee, v in d.items():
            if v > max_value:
                max1, max_value = kee, v
        maximus = [max1, max_value]
        period.append(maximus)
        d[max1] = 0
        max1 = 0
        max_value = 0
    return period


def fill(file):  # Функция для заполнения словаря
    dict1 = dict()
    for lin in file:
        l1 = lin.split()
        for s in l1:
            for k in s.lower():
                dict1[k] = dict1.get(k, 0) + 1
    return dict1


def new_cezar(encrypt, key1):
    alphabet3 = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
    encrypted = ''
    for super in encrypt:
        if super in alphabet3:
            pos = alphabet3.find(super) + 32
            new_pos = pos - (key1 % 32)
            encrypted += alphabet3[new_pos]
        else:
            encrypted += super
    return encrypted


key = 3
f = open('war.txt', 'r', encoding='utf-8')
f2 = open('war2.txt', 'w', encoding='utf-8')
f2.close()
for line in f:
    a = line
    b = cezar(a, key)
    f2 = open('war2.txt', 'a', encoding='utf-8')
    f2.write(b)
    f2.close()
f.close()
# список часто встречаемых слов
rate1 = [['о', 11], ['е', 8.45], ['а', 8.01], ['и', 7.35], ['н', 6.70], ['е', 6.26], ['с', 5.47], ['р', 4.73]]
f2 = open('war2.txt', 'r', encoding='utf-8')
dict1 = fill(f2)
f2.close()
rate2 = periods(dict1)
print('Частоты встречающихся символов из википедии и текста соответственно')
list1 = []  # Список часто встреающихся букв из вики
list2 = []  # Списоквстречающихся букв из текста
for i in range(8):
    list1.append(rate1[i][0])
    list2.append(rate2[i][0])
print(list1)
print(list2)
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
for g in range(3):
    for k in range(3):
        f3 = open('war3.txt', 'w', encoding='utf-8')
        f3.close()
        print("______________________________________________________________________")
        print("Пробный вариант вариант", k, 'значение', g)
        position = alphabet.find(list1[k]) + 32
        position2 = alphabet.find(list2[2]) + 32
        possible_key = abs(position - position2)
        f2 = open('war2.txt', 'r', encoding='utf-8')
        for line in f2:
            a = line
            b = new_cezar(a, possible_key)
            f3 = open('war3.txt', 'a', encoding='utf-8')
            f3.write(b)
            f3.close()
        f2.close()
        f3 = open('war3.txt', 'r', encoding='utf-8')
        print(f3.read())
        f3.close()