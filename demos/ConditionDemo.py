#if
#else
#elif
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')