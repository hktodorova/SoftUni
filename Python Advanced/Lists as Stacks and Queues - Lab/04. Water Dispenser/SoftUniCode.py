from collections import deque

quantity = int(input())
queue = deque()

received_start = False
command_line = input()
while command_line != "End":
    if not received_start:
        if command_line == "Start":
            received_start = True
        else:
            queue.append(command_line)
    else:
        command_line = command_line.split()
        command = command_line[0]

        if command == "refill":
            quantity += int(command_line[1])
        else:
            if int(command_line[0]) <= quantity:
                quantity -= int(command_line[0])
                print(f"{queue.popleft()} got water")
            else:
                print(f"{queue.popleft()} must wait" )

    command_line = input()

print(f"{quantity} liters left")