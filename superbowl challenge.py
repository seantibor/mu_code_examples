my_string = 'neveroddoreven'

print(my_string[::-1])

if my_string == my_string[::-1]:
    print(f"{my_string} is a palindrome")
else:
    print(f"{my_string} is NOT a palindrome")