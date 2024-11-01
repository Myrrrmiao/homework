def is_palindrome(s):
    s = str(s) #делаем так чтобы, если чел ввёл число, оно преобразовалось в строку, чтобы потом мы могли работать с функцией len
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
           return False
        left += 1
        right -= 1
    return True

a = input("Введите строку: ")
print(is_palindrome(a))
