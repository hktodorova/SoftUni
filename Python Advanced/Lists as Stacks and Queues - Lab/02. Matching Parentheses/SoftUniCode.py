from collections import deque

input_string = input()
stack = deque()

for i in range(len(input_string)):
    # Push opening brackets onto the stack
    if input_string[i] in '(':
        stack.append(i)

    # Check for matching closing bracket
    elif input_string[i] in ')':
        if not stack:
            print(False)  # Mismatched bracket
            break
        start_index = stack.pop()  # Pop matched opening bracket
        print(input_string[start_index:i + 1])