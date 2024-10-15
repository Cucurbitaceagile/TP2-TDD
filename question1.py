def affiche(n1, n2):
    result = ""
    for i in range(n1, n2 + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += "FrisBee"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
    print(result)

# Exemple d'exécution
affiche(5, 10)  # BuzzFizz78FizzBuzz
affiche(10, 16) # Buzz11Fizz1314FrisBee16
