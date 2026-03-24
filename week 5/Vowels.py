vowel = "aeiou"
phrase = input("Entrer a phrase: ").lower()
c=0
for ch in phrase:
    if ch in vowel:
        c+=1
print(("There is/are {0} vowels").format(c))
