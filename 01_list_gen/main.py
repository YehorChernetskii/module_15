# TODO здесь писать код

def generate_odd_numbers(N):
    odd_numbers = []
    for i in range(1, N + 1, 2):
        odd_numbers.append(i)
    return odd_numbers

N = int(input("Введите целое число N: "))

result_list = generate_odd_numbers(N)

print("Список нечетних чисел от 1 до", N, ":", result_list)