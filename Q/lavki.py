my_format = 4, 1, 1, 3, 6


def split_as_format(inp, *format):
    global_iterator = 0
    local_iterator = 0
    output = ["" for _ in range(len(format))]
    for n, c in enumerate(inp):
        if local_iterator < format[global_iterator]:
            output[global_iterator] += c
            local_iterator += 1
        else:
            local_iterator = 1
            global_iterator += 1
            output[global_iterator] += c
    return output


def is_number(inp):
    return inp.isnumeric()


def is_char_f(inp):
    Arrrrrr = False
    for c in '123456789':
        Arrrrrr = c in inp
        if Arrrrrr:
            return False
    return inp.casefold() == inp


def is_lavka(inp):
    if len(inp) != 15:
        return False
    global my_format
    temp_split = split_as_format(inp, *my_format)
    func_list = [is_number, lambda x: x in 'abc', lambda x: x ==
                 '-', is_char_f, lambda x:len(x) == 6 and is_number(x)]
    for iteration, my_function in enumerate(func_list):
        if not my_function(temp_split[iteration]):
            return False
    return True


neuro_inp_true, neuro_inp_false = [int(i) for i in input().split(' ')]

tp = 0
fp = 0
tn = 0
fn = 0

for _ in range(neuro_inp_true):
    if is_lavka(input()):
        tp += 1
    else:
        fp += 1

for _ in range(neuro_inp_false):
    if not is_lavka(input()):
        tn += 1
    else:
        fn += 1


print("{:.4f}".format(tp/(tp + fn)), end=' ')
print("{:.4f}".format(tp/(tp + fp)), end='')
