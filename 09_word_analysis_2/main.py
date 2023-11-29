# TODO здесь писать код

def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

input_word = input("Введите слово: ")

if is_palindrome(input_word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")