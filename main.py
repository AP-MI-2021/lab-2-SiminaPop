#pb3
def is_prime(n):
    """
    :param n:  numar natural
    :return: True daca numarul n este prim si False daca numarul n nu este prim
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, n // 2, 2):
        if n % d == 0:
            return False
    return True



def test():
    assert is_prime(3)==True


def get_goldbach(n):
    """
    :param n: n numar natural
    :return: scrierea numarului n ca suma de 2 numere prime
    """

    for i in range(2, n):
        if is_prime(i):
            if is_prime(n - i):
                return i, n - i
    return False


def test_get_goldbach():
    assert get_goldbach(16) == (3, 13)
    assert get_goldbach(15) == (2, 13)

#pb12
def pp(n):
    '''Verifica daca un nr este patrat perfect
    :param: n
    :return: 1 daca nr este pp, 0 daca nu'''
    for i in range(1, n//2+1):
        if n==i*i:
            return 1
    return 0


def testpp():
    assert pp(4)==1
    assert pp(3)==0

def get_perfect_squares(start,stop):
    '''Adauga in lista elementele de tip pp
    :param: start (lista)
    :return: list (alta lista)'''
    list=[]
    for x in range(start,stop):
        if pp(x)==1:
            list.append(x)
    return list


def test_get_perfect_squares():
    assert get_perfect_squares(2,5)==[4]
    assert get_perfect_squares(3,17)==[4,9,16]


#Pb5
def is_palindrome(n):
    '''Verifica daca un numar este palindrom
    :param: n: un numar intreg
    :return: true daca numarul este palindrom si false in rest '''
    aux=n
    pal=0
    while n>0:
        ultima_cifra=n%10
        pal=pal*10+ultima_cifra
        n=n//10
    if aux==pal:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(12321)==True
    assert is_palindrome(1123) == False
    assert is_palindrome(232) == True

def meniu():
    print('''
1.Pb3
2.Pb12
3.Pb5
4.Afara''')


def main():
    # interfata de tip consola aici
    test()
    test_get_goldbach()
    testpp()
    test_get_perfect_squares()
    test_is_palindrome()

    while True:
        meniu()
        cmd = input("Comanda:")
        if cmd == '1':
            n = int(input("introduceti un numar intreg n"))
            print(get_goldbach(n))
        elif cmd == '2':
            elem1= int(input("introduceti capatul inferior al intervalului inchis"))
            elem2=int(input("introduceti capatul superior al intervalului inchis"))
            print(get_perfect_squares(elem1,elem2))
        elif cmd == '3':
            n = int(input("introduceti un numar posibil palindrom  "))
            print(is_palindrome(n))
        elif cmd == '4':
            break
        else:
            print('comanda invalida')

if __name__ == '__main__':
    main()
