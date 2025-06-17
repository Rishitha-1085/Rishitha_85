str=input("Enter the mail in this format name@organization.com : ")
name=''
organization=''
lenn=len(str)-4
for i in range(0,len(str)):
    if str[i]=='@':
        name=str[0:i]
        organization=str[i+1:lenn]
print(f'NAME ID:',name)
print(f'organization is:',organization)
        
