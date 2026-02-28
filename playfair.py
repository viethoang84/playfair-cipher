# Playfair Cipher Implementation
# Matrix fixed as given in class (MONARCHY)

matrix = [
    ['M','O','N','A','R'],
    ['C','H','Y','B','D'],
    ['E','F','G','I','K'],   # I/J merged
    ['L','P','Q','S','T'],
    ['U','V','W','X','Z']
]

def preprocess(text):
    text = text.upper().replace(" ", "")
    text = text.replace("J", "I")

    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                pairs.append(a + 'X')
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + 'X')
            i += 1
    return pairs

def find_position(char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c

def encrypt_pair(pair):
    r1, c1 = find_position(pair[0])
    r2, c2 = find_position(pair[1])

    # Same row
    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]

    # Same column
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]

    # Rectangle rule
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt(text):
    pairs = preprocess(text)
    cipher = ""
    for pair in pairs:
        cipher += encrypt_pair(pair)
    return cipher

plaintext = "Do you like to study a crytography course"
ciphertext = encrypt(plaintext)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)