def createStack():
return [ ]
def push(stack, element): stack.append(element)
def pop(stack):
return stack.pop()
def isEmpty(stack): return len(stack)==0
newStack=createStack()
Ewhile True:
print("The stack so far is:", newStack)
print("-------")
print("Choose 1 for push")
print("Choose 2 for pop")
print("Choose 3 for end")
print(" choice=int(input("Enter your choice: "))

while choice!=1 and choice!=2 and choice!=3:
print ("Erroг")
choice=int(input("Enter your choice: "))
if choice==1:
x=int(input("Enter element for push: "))
push(newStack, x)
else:
elif choice==2:
if not isEmpty(newStack):
print("The pop element is:", pop (newStack))
else:
print("The stack is empty")
print("End of program")
break;
