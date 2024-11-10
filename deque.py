from collections import deque

first_list = deque([1, 3, 5, 7])
second_list = deque([2, 4, 6, 8])
result = deque()

while first_list or second_list:
    if first_list:
        result.append(first_list.popleft())
    if second_list:
        result.append(second_list.popleft())

result_list = sorted(set(result))

print(f'deque == {result_list}')
