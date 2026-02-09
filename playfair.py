def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in matrix:
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def preprocess(text):
    text = text.upper().replace("J", "I")
    res = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            res += a + "X"
            i += 1
        else:
            res += a + b
            i += 2
    if len(res) % 2 != 0:
        res += "X"
    return res

def playfair_encrypt(plaintext, key):
    matrix = generate_matrix(key)
    text = preprocess(plaintext)
    cipher = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i+1])

        if r1 == r2:
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

def playfair_decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    plain = ""

    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(matrix, ciphertext[i])
        r2, c2 = find_pos(matrix, ciphertext[i+1])

        if r1 == r2:
            plain += matrix[r1][(c1-1) % 5]
            plain += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            plain += matrix[(r1-1) % 5][c1]
            plain += matrix[(r2-1) % 5][c2]
        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


# Example
key = "MONARCHY"
pt = "BALLOON"
ct = playfair_encrypt(pt, key)
print("Cipher:", ct)
print("Decrypted:", playfair_decrypt(ct, key))
