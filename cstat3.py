st=str(input("Enter strings with brackets:"))
stack=[]
dict={')':'(','}':'{',']':'['}

value=True

for ch in st:
    if ch in "({[":
       stack.append(ch)
    else:
       if len(st) == 0 or stack[-1]!=dict[ch]:
          value=False
          break
       stack.pop()
if value and len(stack) == 0:
   print("Valid")
else:
   print("Invalid")
