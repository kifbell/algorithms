import operator
import functools


def mat(toes: int, heads: int, pdf: list) -> int:
    """takes number of toes, number of heads, discrete probability density func
    calculates probability of k heads occurred in n toes"""

    pdf = [0] + pdf
    inverse_pdf = list(map(lambda p: 1 - p, pdf))
    inv_pty_prdct = lambda n: functools.reduce(operator.mul, inverse_pdf[0:n + 1])
    # creates the matrix below
    pty_mat = [[((inv_pty_prdct(n), 0)[k > 0], int(k == 0))[n == 0] for k in range(heads + 1)] for n in range(toes + 1)]
    # [1, 0, 0, 0, 0, 0]
    # [0.5, 0, 0, 0, 0, 0]
    # [0.25, 0, 0, 0, 0, 0]
    # [0.125, 0, 0, 0, 0, 0]
    # [0.0625, 0, 0, 0, 0, 0]
    # [0.03125, 0, 0, 0, 0, 0]

    for n in range(1, toes + 1):
        for k in range(1, heads + 1):
            pty_mat[n][k] = inverse_pdf[n] * pty_mat[n - 1][k] + pdf[n] * pty_mat[n - 1][k - 1]

    for n, line in enumerate(pty_mat):
        print(f'n = {n}:', *line, sep='\t\t')
    print()
    return pty_mat[toes][heads]


print(mat(5, 5, [0.5] * 5))
