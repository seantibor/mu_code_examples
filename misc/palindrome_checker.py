def is_palin(word):
    if word == reverse(word):
        return True
    else:
        return False


def reverse(s):
    print(s[::-1])
    return s[::-1]


while True:
    print(is_palin(input("word?:")))
