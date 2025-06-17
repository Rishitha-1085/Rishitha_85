str=input("Enter the string: ")
digit_count=0
vowel_count=0
consonent_count=0
specialchar=0
for ch in str.lower():
    if ch.isdigit():
        digit_count+=1
    elif ch.isalpha():
        if ch in ['a','e','i','o','u']:
            vowel_count+=1
        else:
            consonent_count+=1
    else:
        specialchar+=1
print(f"DIGIT COUNT : {digit_count}")
print(f"VOWEL  COUNT : {vowel_count}")
print(f"CONSONENT COUNT: {consonent_count}")
print(f"SPECIAL CHARECTOR : {specialchar}")
