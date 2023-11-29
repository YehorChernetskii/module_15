# TODO здесь писать код

n = int(input("Кол-во клеток: "))

efficiency_values = []

for i in range(1, n + 1):
    efficiency = int(input(f"Эффективность {i} клетки: "))
    efficiency_values.append(efficiency)

print("Неподходящие значения:", end=' ')
for i in range(n):
    if efficiency_values[i] < i + 1:
        print(efficiency_values[i], end=' ')
print()