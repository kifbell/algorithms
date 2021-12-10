from math import log2
import operator as op


class Symbols:
    def __init__(self, value: str, ind: int = 0):
        self.value = value
        self.ec = ''
        self._ind = ind

    def extend_ec(self, new_ec: str = "-1"):
        self.ec += new_ec

    def get_index(self):
        return self._ind


def extended_string(text: str):
    text_len = len(text)
    expected_len = int(log2(text_len)) + 1
    return text + "$" * (expected_len - text_len)


def assign_indices(text: str):
    '''returns list of lists consicting of letter and '''
    return list(map(list, enumerate(text)))


def main_func(text: str):
    extended_text = extended_string(text)
    main_arr = [Symbols(letter, ind) for ind, letter in enumerate(extended_text)]

    get_letter = op.attrgetter("value")
    main_arr.sort(key=lambda symbol: get_letter(symbol))



def input_func(file_name):
    pass
    with open(file_name, "r") as stream:
        text = stream.readline()

    return text


def main():
    pass
