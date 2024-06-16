# - Write a function that receives two words (String) and returns
# - true or false (Bool) depending on whether they are anagrams or not.
# - An Anagram consists of forming a word by rearranging ALL the letters of another initial word.
# - the letters of another initial word.
# - It is NOT necessary to check that both words exist.
# - Two words that are exactly the same are not anagrams.


import unittest

def is_anagram(text1, text2):
    
    if text1 == text2:
        return False
    
    text1 = text1.lower()
    text2 = text2.lower()
    
    return sorted(text1) == sorted(text2)

class TestAnagram(unittest.TestCase):
    
    def test_anagrams(self):
        self.assertTrue(is_anagram("amor", "Roma"))
        self.assertTrue(is_anagram("test", "sett"))
        self.assertTrue(is_anagram("elvis", "lives"))
        self.assertTrue(is_anagram("finder", "friend"))
        self.assertTrue(is_anagram("schoolmaster", "theclassroom"))

    def test_not_anagrams(self):
        self.assertFalse(is_anagram("amor", "amor"))
        self.assertFalse(is_anagram("anagrama", "margana"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("apple", "pale"))

    def test_empty_strings(self):
        self.assertFalse(is_anagram("", ""))
        self.assertFalse(is_anagram("a", ""))
        self.assertFalse(is_anagram("", "a"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("a", "aa"))
        self.assertFalse(is_anagram("abc", "abcd"))

if __name__ == '__main__':
    unittest.main()
