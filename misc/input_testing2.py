while True:
    name = input('What\'s your name? ')
    if name.lower() != '':
        print('hi, good morning, ' + name)
        break
    else:
        print('something rude')

    print(name)

score = int(input('What did you get on the math test?'))
if score > 90:
    print('great job')
elif score > 80:
    print('good job. I know you worked hard')
