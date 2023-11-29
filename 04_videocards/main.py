# TODO здесь писать код

n = int(input("Кол-во видеокарт: "))

graphics_cards = []

for i in range(1, n + 1):
    model = int(input(f"{i} Видеокарта: "))
    graphics_cards.append(model)

print("Старый список видеокарт:", graphics_cards)

max_value = max(graphics_cards)

graphics_cards = [value for value in graphics_cards if value != max_value]

print("Новый список видеокарт:", graphics_cards)
