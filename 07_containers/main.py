# TODO здесь писать код

n = int(input("Кол-во контейнеров: "))

weights = []

for _ in range(n):
    weight = int(input("Введите вес контейнера: "))
    weights.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))

position = 1
while position <= n and weights[position - 1] >= new_weight:
    position += 1

print("Номер, куда встанет новый контейнер:", position)