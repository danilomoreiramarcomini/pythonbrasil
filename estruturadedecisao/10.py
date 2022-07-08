# https://wiki.python.org.br/EstruturaDeDecisao

print('[M] - Morning | [A] - Afternoon | [N] - Nightly')
time_course = str(input('What time do you study:')).upper()

if time_course.isalpha() is True:
    if len(time_course) == 1:
        if time_course == 'M':
            print('\033[34mGood Morning\033[38m!')
        elif time_course == 'A':
            print('\033[34mGood Afternoon\033[38m!')
        elif time_course == 'N':
            print('\033[34mGood Evening\033[38m!')

        elif time_course != 'M' or time_course != 'A' or time_course != 'N':
            print('\033[31mInvalid\033[38m')
    else:
        print('\033[31mInvalid\033[38m')
else:
    print('\033[31mInvalid\033[38m')
