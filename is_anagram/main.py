# - Write a function that receives two words (String) and returns
# - true or false (Bool) depending on whether they are anagrams or not.
# - An Anagram consists of forming a word by rearranging ALL the letters of another initial word.
# - the letters of another initial word.
# - It is NOT necessary to check that both words exist.
# - Two words that are exactly the same are not anagrams.


def is_anagram(text1, text2):
    
    if text1 == text2:
        return False
    
    text1 = text1.lower()
    text2 = text2.lower()
    
    return sorted(text1) == sorted(text2)


    
print(is_anagram("amor", "Roma"))  #   True
print(is_anagram("amor", "amor"))  #   False
print(is_anagram("anagrama", "margana"))  #   False
print(is_anagram("test", "sett"))  #   True
print(is_anagram("python", "java"))  #   False