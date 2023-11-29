# TODO здесь писать код

def cyclic_shift_arithmetic(lst, k):
    n = len(lst)

    shifted_indices = [(i + k) % n for i in range(n)]

    shifted_list = [lst[i] for i in shifted_indices]

    return shifted_list

original_list = list(map(int, input("Введите элементы списка через запятую: ").split(',')))
shift_value = int(input("Введите к-во пунктов для сдвига вправо: "))

result = cyclic_shift_arithmetic(original_list, shift_value)
print("Изначальный список:", original_list)
print("Сдвинутый список:", result)