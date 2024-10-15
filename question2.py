import string

def crypt(message):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result = ""
    
    for char in message:
        if char == " ":
            result += "!"
        elif char in caracteres:
            index = caracteres.index(char)
            result += caracteres[(index + 1) % len(caracteres)]
        else:
            result += char  
    return result

# Tests du TDD
def test_crypt():
    assert crypt("abc") == "bcd", "Test 1 échoué"
    assert crypt("ABC") == "BCD", "Test 2 échoué"
    assert crypt("123") == "234", "Test 3 échoué"
    assert crypt(" ") == "!", "Test 4 échoué"

test_crypt()

# Exemple d'exécution
print(crypt("abc"))  # Devrait afficher: bcd
print(crypt("ABC"))  # Devrait afficher: BCD
print(crypt("123"))  # Devrait afficher: 234
print(crypt(" "))    # Devrait afficher: !
