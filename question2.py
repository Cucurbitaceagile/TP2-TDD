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

def decrypt(message):
    pas = int(message[-1])
    
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    result = ""
    
    for char in message[:-1]:
        if char == "!":
            result += " "
        elif char in caracteres:
            index = caracteres.index(char)
            result += caracteres[(index - pas) % len(caracteres)]
        else:
            result += char
    
    return result

# Tests TDD
def test_crypt_decrypt():
    assert crypt("abc", 1) == "bcd1", "Test 1 échoué"
    assert decrypt("bcd1") == "abc", "Test 2 échoué"
    
    assert crypt("ABC", 2) == "CDE2", "Test 3 échoué"
    assert decrypt("CDE2") == "ABC", "Test 4 échoué"
    
    assert crypt("123", 3) == "4563", "Test 5 échoué"
    assert decrypt("4563") == "123", "Test 6 échoué"
    
    assert crypt(" ", 4) == "!4", "Test 7 échoué"
    assert decrypt("!4") == " ", "Test 8 échoué"

test_crypt_decrypt()

# Exemple d'exécution
print(crypt("abc", 1))   # Devrait afficher: bcd1
print(decrypt("bcd1"))   # Devrait afficher: abc
print(crypt(" ", 4))     # Devrait afficher: !4
print(decrypt("!4"))     # Devrait afficher:  
