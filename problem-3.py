a = int(input("Enter a number: "))

n = a if a % 2 != 0 else a - 1

series = [2 * i - 1 for i in range(1, n + 1)]
print(", ".join(map(str, series)))
