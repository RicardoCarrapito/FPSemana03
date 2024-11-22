from collections import deque

stack=deque()

palavra=input()

for i in palavra.split():
    stack.appendleft(i)

print(stack)

while stack:
    i = stack.pop()
    if "a" in i:
        print(i)



        
