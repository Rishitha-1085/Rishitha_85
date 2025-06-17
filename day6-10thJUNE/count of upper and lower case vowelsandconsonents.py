str=input("Enter the string: ")
Lvowel_count=0
Lconsonent_count=0
Uvowel_count=0
Uconsonent_count=0

for i in range(len(str)):
    if (str[i].isalpha()):
        if (str[i].islower()):
            if (str[i] in ['a','e','i','o','u']):
                Lvowel_count+=1
            else:
                Lconsonent_count+=1
        if (str[i].isupper()):
            if (str[i] in ['A','E','I','O','U']):
                Uvowel_count+=1
            else:
                Uconsonent_count+=1
print(f"UPPERCASE  VOWEL  COUNT : {Uvowel_count}")
print(f"LOWERCASE VOWEL  COUNT : {Lvowel_count}")
print(f"LOWERCASE CONSONENT COUNT: {Lconsonent_count}")
print(f"UPPERCASE CONSONENT COUNT: {Uconsonent_count}")

