from pprint import pprint
from string import ascii_uppercase, digits


keyword = "HIMOMILOVEYOU"
ADFGVX = "ADFGVX"
column_key = [5, 1, 3, 2, 6, 4]

non_repeated = []
for filler in keyword + ascii_uppercase + digits:
    if filler not in non_repeated:
        non_repeated.append(filler)

polybius_square = []
i = 0
for _ in range(len(ADFGVX)):
    row = []
    for _ in range(len(ADFGVX)):
        row.append(non_repeated[i])
        i += 1
    polybius_square.append(row)


pprint(polybius_square)


def coordinate_map(character):
    for x in range(len(ADFGVX)):
        for y in range(len(ADFGVX)):
            if polybius_square[x][y] == character:
                return ADFGVX[x] + ADFGVX[y]

def coordinate_demap(coordinate):
    x, y = ADFGVX.index(coordinate[0]), ADFGVX.index(coordinate[1])
    return polybius_square[x][y]


def encrypt(plain_text):
    intermediate = ""
    for character in plain_text:
        intermediate += coordinate_map(character)
    
    intermediate_matrix = []
    row = []
    for character in intermediate:
        row.append(character)
        if len(row) == len(column_key):
            intermediate_matrix.append(row.copy())
            row.clear()
    if row:
        intermediate_matrix.append(row)
    
    cipher_text = ""
    for i in range(1, len(column_key) + 1):
        column = column_key.index(i)
        row = 0
        while row < len(intermediate_matrix) and column < len(intermediate_matrix[row]):
            cipher_text += intermediate_matrix[row][column]
            row += 1
    
    return cipher_text


def decrypt(cipher_text):
    q, r = divmod(len(cipher_text), len(column_key))
    intermediate_matrix = [[''] * len(column_key) for _ in range(q)]
    intermediate_matrix.append([''] * r)

    character_index = 0
    for i in range(1, len(column_key) + 1):
        column = column_key.index(i)
        for row in range(q):
            intermediate_matrix[row][column] = cipher_text[character_index]
            character_index += 1
        if column < r:
            intermediate_matrix[-1][column] = cipher_text[character_index]
            character_index += 1
    
    intermediate_text = "".join("".join(row) for row in intermediate_matrix)
    plain_text = ""
    for i in range(0, len(intermediate_text), 2):
        plain_text += coordinate_demap(intermediate_text[i:i + 2])

    
    return plain_text


encrypted_text = encrypt("ALICE")
decrypted_text = decrypt(encrypted_text)

print(encrypted_text, decrypted_text)
