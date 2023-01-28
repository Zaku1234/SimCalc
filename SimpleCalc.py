
def calculator():
    print("Wybierz dzaialanie.")
    print("1. Podstawowe operacje")
    print("2. Dzialania na macierzach")
    print("3. Zamiana systemow")
    print("4. Zakoncz")
    choice = int(input("Wybierz opcje (1/2/3/4): "))

    if choice == 1:
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnozenie")
        print("4. Dzielenie")
        choice = int(input("Wybierz opcje (1/2/3/4): "))
        num1 = float(input("Pierwsza liczba: "))
        num2 = float(input("Druga liczba: "))
        if choice == 1:
            print("Wynik dzialania", num1, "+", num2, "=" , num1 + num2)
        elif choice == 2:
            print("Wynik dzialania", num1, "-", num2, "=" , num1 - num2)
        elif choice == 3:
            print("Wynik dzialania", num1, "*", num2, "=" , num1 * num2)
        elif choice == 4:
            print("Wynik dzialania", num1, "/", num2, "=" , num1 / num2)
        else:
            print("Niepoprawny wybor")
    elif choice == 2:
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnozenie")
        print("4. Transponowanie")
        choice = int(input("Wybierz opcje (1/2/3): "))
        if choice == 1:
            macierz1 = [[float(input("Podaj wartosc dla macierzy 1: ")) for i in range(3)] for j in range(3)]
            macierz2 = [[float(input("Podaj wartosc dla macierzy 2: ")) for i in range(3)] for j in range(3)]
            result = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    result[i][j] = macierz1[i][j] + macierz2[i][j]
            print("Macierz 1:",macierz1)
            print("Macierz 2:",macierz2)
            print("Wynik: ",result)
        elif choice == 2:
            macierz1 = [[float(input("Podaj wartosc dla macierzy 1: ")) for i in range(3)] for j in range(3)]
            macierz2 = [[float(input("Podaj wartosc dla macierzy 2: ")) for i in range(3)] for j in range(3)]
            result = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    result[i][j] = macierz1[i][j] - macierz2[i][j]
            print("Macierz 1:",macierz1)
            print("Macierz 2:",macierz2)
            print("Wynik: ",result)
        elif choice == 3:
            macierz1 = [[float(input("Podaj wartosc dla macierzy 1: ")) for i in range(3)] for j in range(3)]
            macierz2 = [[float(input("Podaj wartosc dla macierzy 2: ")) for i in range(3)] for j in range(3)]
            result = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result[i][j] += macierz1[i][k] * macierz2[k][j]
            print("Macierz 1:",macierz1)
            print("Macierz 2:",macierz2)
            print("Wynik: ",result)
        elif choice == 4:
            macierz1 = [[float(input("Podaj wartosc dla macierzy transponowanej: ")) for i in range(3)] for j in range(3)]
            result = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                        result[i][j] = macierz1[j][i]
            print("Wynik: ",result)
        else:
            print("Niepoprawny wybor")
    elif choice == 3:
        print("1. Dziesiatkowy na Dwojkowy")
        print("2. Dziesiatkowy na Osemkowy")
        print("3. Dziesiatkowy na Szesnastkowy")
        choice = int(input("Wybierz (1/2/3): "))
        num = int(input("Podaj liczbe w systemie dziesietnym: "))
        if choice == 1:
            print("Liczba w systemie dwojkowym: ", bin(num)[2:])
        elif choice == 2:
            print("Liczba w systemie osemkowym: ", oct(num)[2:])
        elif choice == 3:
            print("Liczba w systemie szesnastkowym: ", hex(num)[2:])
        else:
            print("Niepoprawny wybor")
    elif choice == 4:
        print("Koncze dzialanie kalkulatora...")
        return
    else:
        print("Niepoprawny wybor")
        
    input("Nacisniecie przycisku pozwoli kontynuowac dzialanie programu")
    calculator()

calculator()
