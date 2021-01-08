def f(n):
    if n < 2:
        return 1
    if n > 100:
        raise ValueError()
    answ = 1
    for i in range(n):
        answ *= i+1
    return answ


def func(string: str):
    if '==' not in string and '=' in string:
        string = string.replace('=', '==')
    if '^' in string:
        string = string.replace('^', '**')
    string = string.replace('f(', '!')
    letters_set = tuple(set(i for i in string if i not in '+-*/=1234567890(.)! '))
    numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    if len(letters_set) > 9:
        print('No answers')
        return


    def per(mas, length):
        if length == 1:
            for i in mas:
                yield str(i)
        for i in mas:
            mas2 = mas.copy()
            mas2.remove(i)
            for j in per(mas2, length-1):
                answ = str(i) + j
                yield answ


    for i in per(numbs, len(letters_set)):
        new_string = string
        for j in enumerate(i):
            new_string = new_string.replace(letters_set[j[0]], str(j[1]))
        new_string = new_string.replace('!', 'f(')
        try:
            if eval(new_string):
                print('\nANSWER: ' + new_string.replace('==', '=').replace('**', '^') + '\n')
                return
        except SyntaxError:
            continue
    print('No answers')


if __name__ == '__main__':
    while True:
        text = input("type the equation\n[example: (aaa + bbc) * d = 100 - a]\nuse f(a) instead of a!\nor 'q' to quit: ")
        if text.lower() == 'q':
            break
        func(text)
