from collections import deque

stack=deque()

numeros=input()

for i in numeros.split():
    stack.append(int(i))

print(stack)

while stack:
    if(stack):
        value=stack.pop()
        print(value*2)




