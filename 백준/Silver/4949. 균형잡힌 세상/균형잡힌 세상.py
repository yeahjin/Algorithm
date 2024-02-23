def bracket(s):
    l = []
    for i in s:
        if i == '(' or i == '[':
            l.append(i)
        if i == ')':
            if len(l) == 0:
                return False
            if l[-1] == '(':
                l.pop()
            else:
                return False
        if i == ']':
            if len(l) == 0:
                return False
            if l[-1] == '[':
                l.pop()
            else:
                return False
    return len(l) == 0


while True:
    s = input()
    if s == ".":
        break
    if bracket(s):
        print("yes")
    else:
        print("no")
