import operator as op
from math import log2


class Symbols:
    def __init__(self, value: str, ind: int = 0):
        self.value = value
        self.ec = ''
        self.ind = ind

    def extend_ec(self, new_ec: str = "-1"):
        self.ec += new_ec

    def get_index(self):
        return self.ind

    def reduce_index(self):
        self.ind -= 1


def extended_string(text: str):
    text_len = len(text)
    log_len = log2(text_len)
    expected_len = 2 ** [int(log_len) + 1, int(log_len)][int(log_len) == log_len]
    return text + "$" * (expected_len - text_len)


def reduce_indices(arr: list[Symbols]):
    max_ind = len(arr)
    ind_reduction = len(arr[0].value)
    for symbol in arr:
        symbol.ind = (symbol.ind - ind_reduction) % max_ind


def assign_symbols_by_ind(text: str, arr: list[Symbols]):
    text *= 2
    for symbol in arr:
        symbol.value = text[symbol.ind: symbol.ind + 2 * len(symbol.value)]


def sort_extend_ec_reset_ec():
    pass


def upgrade_ec(arr: list[Symbols], ec_store):
    for symbol in arr:
        symbol.ec = ec_store[symbol.value[:len(symbol.value) // 2]] + str(symbol.ec)


def initiate_ec(arr: list[Symbols]):
    ec_cnt = 0
    passed_value = str(arr[0].value)
    ec_store = dict()
    for symbol in arr:
        if symbol.value != passed_value:
            passed_value = str(symbol.value)
            ec_cnt += 1
        symbol.ec += str(ec_cnt)
        ec_store[str(symbol.value)] = str(symbol.ec)
    return ec_store


def reset_ec(arr: list[Symbols], ec_store):
    ec_cnt = 0
    passed_ec = str(arr[0].ec)
    for symbol in arr:
        if symbol.ec != passed_ec:
            passed_ec = str(symbol.ec)
            ec_cnt += 1
        symbol.ec = str(ec_cnt)
        ec_store[str(symbol.value)] = str(symbol.ec)
    return ec_store


def main_func(text: str):
    get_letter = op.attrgetter("value")
    text = 'abacababacaba'

    extended_text = extended_string(text)
    main_arr = [Symbols(letter, ind) for ind, letter in enumerate(extended_text)]

    main_arr.sort(key=lambda sym: get_letter(sym))
    ec_dict = initiate_ec(main_arr)
    ec_dict = reset_ec(main_arr, ec_dict)

    print(extended_text)
    for _ in range(int(log2(len(extended_text)))):
        reduce_indices(main_arr)
        assign_symbols_by_ind(extended_text, main_arr)
        main_arr.sort(key=lambda sym: get_letter(sym))
        upgrade_ec(main_arr, ec_dict)
        ec_dict = reset_ec(main_arr, ec_dict)
        for symbol in main_arr:
            print(f"{symbol.value}: ec: {symbol.ec}, start ind: {symbol.ind}")
        print()


def input_func(file_name):
    pass
    with open(file_name, "r") as stream:
        text = stream.readline()
    return text


def main():
    pass


main_func('asdf')
