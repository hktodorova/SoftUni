customer_queue = []

command_line = input()
while command_line != "End":
    if command_line == "Paid":
        while customer_queue:
            print(customer_queue.pop(0))
    else:
        customer_queue.append(command_line)

    command_line = input()

print(f"{len(customer_queue)} people remaining.")