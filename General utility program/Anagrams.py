#Anagram

s1 = input("Enter first String:")
s2 = input("Enter Last String: ")
if sorted(s1)==sorted(s2):
    print("The strings are anagrams!")
else:
    print("The strings are not anagrams!")
