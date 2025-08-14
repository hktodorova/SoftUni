from collections import deque

kids = deque(input().split())
toss = int(input())

while len(kids) > 1:
    counter = toss % len(kids)
    if counter == 0:
        print(f"Removed {kids.pop()}")
    else:
        for i in range(counter - 1):
            kid = kids.popleft()
            kids.append(kid)
        print(f"Removed {kids.popleft()}")

print(f"Last is {''.join(kids)}")