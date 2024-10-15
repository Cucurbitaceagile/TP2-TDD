import string

def crypt(message, pas):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result = ""

    for char in message:
        if char == " ":
            result += "!" 
        elif char in caracteres:
            index = caracteres.index(char)
            result += caracteres[(index + pas) % len(caracteres)]
        else:
            result += char  
    return result + str(pas)

# Tests TDD
def test_crypt():
    assert crypt("abc", 1) == "bcd1", "Test 1 échoué"
    assert crypt("ABC", 2) == "CDE2", "Test 2 échoué"
    assert crypt("123", 3) == "4563", "Test 3 échoué"
    assert crypt(" ", 4) == "!4", "Test 4 échoué" 

test_crypt()

# Exemple d'exécution
print(crypt("abc", 1))  # Devrait afficher: bcd1
print(crypt("ABC", 2))  # Devrait afficher: CDE2
print(crypt("123", 3))  # Devrait afficher: 4563
print(crypt(" ", 4))    # Devrait afficher: !4
