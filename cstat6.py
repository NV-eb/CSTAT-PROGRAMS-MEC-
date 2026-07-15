s=input("Enter a string:")
v=0
c=0
q=0

for ch in s:
    if ch.isalpha():
       if(ch=='a' or ch=='e'or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U'):
         v+=1
       else:
         c+=1
    else:
       if(ch=='?'):
         q+=1
w=len(s.split())
print("No of vowels:",v)
print("No of consonants:",c)
print("No of words:",w)
print("No of question marks:",q)
