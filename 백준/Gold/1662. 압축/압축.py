s = input()

length = 0
stack = []
char = ""

for i in s:
    if i == ")":
        p, m = stack.pop()
        length = ((m*length) + p)
    elif i == "(":
        stack.append([length - 1, int(char)])
        length = 0
    else:
        length += 1
        char = i

print(length)