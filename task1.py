def check_parentheses(array):
    stack = []
    dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for i in array:
        if i in dict.keys():
            stack.append(i)

        elif i in dict.values():
          if not stack or dict[stack.pop()] != i:
           return False

        else:
           return False

    return not stack

a = "(({[]}))" # True
b1 = "{(})"    # False
c = '([])[[]]' # True
b2 = ")())[[]]" # False
b3 = "(())[[]]" # True
b4 = '([])'    # True

print(check_parentheses(a))
print(check_parentheses(b1))
print(check_parentheses(c))
print(check_parentheses(b2))
print(check_parentheses(b3))
print(check_parentheses(b4))

