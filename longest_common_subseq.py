# class LCS:
#     def __init__(self, value):
#         self.checked = False
#         self.value = value

def top_down_lcs(a: str, b: str) -> int:
    a_len = len(a)
    b_len = len(b)
    mat = [[-1 for _ in range(b_len + 1)] for _ in range(a_len + 1)]
    start = [0, 0]

    def fill_mat(i: int, j: int):
        global start
        if i == 0 or j == 0:
            mat[i][j] = 0
            start = (i, j)
        elif a[i - 1] == b[j - 1]:
            if mat[i - 1][j - 1] == -1:
                fill_mat(i - 1, j - 1)
                # print(a[i - 1], end='')
            mat[i][j] = mat[i - 1][j - 1] + 1

        elif a[i - 1] != b[j - 1]:
            if mat[i][j - 1] == -1:
                fill_mat(i, j - 1)
            if mat[i - 1][j] == -1:
                fill_mat(i - 1, j)
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    def recover_lcs():
        longest_common_subsequence = ""
        i, j = start
        prefix_length = -2
        while i < a_len and j < b_len:
            if mat[i + 1][j] == mat[i][j + 1]:
                i, j = i + 1, j + 1
            elif mat[i + 1][j] > mat[i][j + 1]:
                i, j = i + 1, j
            else:
                i, j = i, j + 1

            if prefix_length < mat[i][j]:
                longest_common_subsequence += a[i - 1]
                prefix_length = mat[i][j]
        return longest_common_subsequence

    fill_mat(a_len, b_len)
    return mat[a_len][b_len], recover_lcs(), mat


lcs_length, lcs, mat = top_down_lcs(input("enter the first string: "), input("enter the second string: "))

# print(*mat, sep='\n', end='\n\n')
print(f"longest common subsequence of length {lcs_length} is: {lcs}")
