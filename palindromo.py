import unittest

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)
    
    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)
    
    def test_aca(self):
        resultado = is_palindrome('aca')
        self.assertEqual(resultado, True)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)



def is_palindrome(string):

    for i in range(0,len(string)):
    
        if string[i] == string[-i-1]:
            pass
        
        else:
            return False
        
    return True


print("Detector de palindromes")
palabra = input("Inserte una palabra: ")

is_palindrome(palabra)

if is_palindrome(palabra) == True:
    print("Su palabra es palindrome")
else:
    print("Su palabra no es palindrome")