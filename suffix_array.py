import operator as op
from typing import List

from math import log2


class Symbols:
    def __init__(self, value, ind = 0):
        self.value = value
        self.ec = ''
        self.ind = ind

    def extend_ec(self, new_ec: str = "-1"):
        self.ec += new_ec

    def get_index(self):
        return self.ind

    def reduce_index(self):
        self.ind -= 1


def extended_string(text):
    text_len = len(text)
    log_len = log2(text_len)
    expected_len = 2 ** [int(log_len) + 1, int(log_len)][int(log_len) == log_len]
    return text + "$" * (expected_len - text_len)


def reduce_indices(arr):
    max_ind = len(arr)
    ind_reduction = len(arr[0].value)
    for symbol in arr:
        symbol.ind = (symbol.ind - ind_reduction) % max_ind


def assign_symbols_by_ind(text, arr):
    text *= 2
    for symbol in arr:
        symbol.value = text[symbol.ind: symbol.ind + 2 * len(symbol.value)]


def upgrade_ec(arr, ec_store):
    for symbol in arr:
        symbol.ec = ec_store[symbol.value[:len(symbol.value) // 2]] + str(symbol.ec)


def initiate_ec(arr):
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


def reset_ec(arr, ec_store):
    ec_cnt = 0
    passed_ec = str(arr[0].ec)
    for symbol in arr:
        if symbol.ec != passed_ec:
            passed_ec = str(symbol.ec)
            ec_cnt += 1
        symbol.ec = str(ec_cnt)
        ec_store[str(symbol.value)] = str(symbol.ec)
    return ec_store


def get_suffix_array(text):
    get_letter = op.attrgetter("value")

    extended_text = extended_string(text)
    main_arr = [Symbols(letter, ind) for ind, letter in enumerate(extended_text)]

    main_arr.sort(key=lambda sym: get_letter(sym))
    ec_storage = initiate_ec(main_arr)
    ec_storage = reset_ec(main_arr, ec_storage)

    # print(extended_text)
    for _ in range(int(log2(len(extended_text)))):
        reduce_indices(main_arr)
        assign_symbols_by_ind(extended_text, main_arr)
        main_arr.sort(key=lambda sym: get_letter(sym))
        upgrade_ec(main_arr, ec_storage)
        ec_storage = reset_ec(main_arr, ec_storage)

        # for symbol in main_arr:
        #     print(f"{symbol.value}: ec: {symbol.ec}, start ind: {symbol.ind}")
        # print()

    return main_arr
    # print(ec_storage)


def input_func(file_name):
    with open(file_name, "r") as stream:
        text = stream.readline().strip()
        return text, [pattern_line.strip() for pattern_line in stream.readlines()]


def find_patterns(suffix_array, patterns):
    ans = list()
    for i, pattern in enumerate(patterns):
        this_pattern = list()
        for symbol in suffix_array:
            if symbol.value.startswith(pattern):
                this_pattern.append(symbol.ind)
        ans.append([i + 1, pattern, sorted(this_pattern)])

    return ans


def output_patterns(patterns):
    upgraded_str = lambda index: str(index + 1)
    for pattern_nubmer, _, start_indices in patterns:
        if start_indices:
            print(f"{pattern_nubmer}: {', '.join(list(map(upgraded_str, start_indices)))}")


if __name__ == "__main__":
    text, patterns = input_func("input.txt")
    suffix_array = get_suffix_array(text)
    ans = find_patterns(suffix_array, patterns)
    output_patterns(ans)
