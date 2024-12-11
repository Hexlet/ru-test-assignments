## Python

## Задача 1
Дан целочисленный массив. Необходимо вывести true, если есть повторения и false, если нет.

Input: [1, 2, 3, 1]
Output: True

Input: [1, 2, 3, 4]
Output: False

**Решение:**
```
nums = [1, 2, 3, 4, 4]
def reps(nums):
    if len(set(nums)) != len(nums):
        return True
    else:
        return False
```

## Задача 2
Дано число n. Вернуть факториал этого числа. Вызвать -1, если n не целочисленно, а так же если n отрицательно.

Input: n = 5
Output: 120

Input: n = 0
Output: 1

**Решение:**
```
def factorial(n):
    if isinstance(n, float) or n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
            i + 1
    return result
```



