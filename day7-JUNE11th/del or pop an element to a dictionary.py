#add an element to dictionary
jobrole={101:'front-end developer',102:'Back-end developer',103:'SQL administration'}
jobrole[101]='UI/UX Developer'
jobrole[104]='data Engineer'
jobrole[105]='Python Developer'
jobrole[106]='data analyst'
print(jobrole)

#delete UI/UX Developer
jobrole.pop(101)
del jobrole[103]
print(jobrole)

