def rpn(array):
    stack = []
    operations = {   #мы определяем так сказать словарь, к которому потом будем обращаться, со всеми нашими операндами
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y
    }

    for token in array: # запускаем цикл, в котором будем пробегаться по нашему массиву
        if token in operations: # если мы встречаем операнд, то...
            operand2 = stack.pop() # забираем последний элемент массива
            operand1 = stack.pop() # забираем первый элемент массива
            temp_result = operations[token](operand1, operand2) # обращаемся к нашему словарю и находим наш операнд и вызываем лямбду функцию
            stack.append(temp_result) #добавляем в массив
        else: # если не операнд встретили, а обычное число
            stack.append(int(token))

    return stack[0]

print(rpn(["3", "5", "+"]))
print(rpn(["2", "1", "+", "3", "*"]))
print(rpn(["4", "13", "5", "/", "+"]))