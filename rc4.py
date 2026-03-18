# RC4 implementation 
# S = [0..9]
# K = [2,4,1,7]
# Plaintext = "cybersecurity"

def KSA():
    S = list(range(10))
    K = [2, 4, 1, 7]
    T = [K[i % len(K)] for i in range(10)]

    j = 0
    print("=== KSA ===")
    for i in range(10):
        j = (j + S[i] + T[i]) % 10
        S[i], S[j] = S[j], S[i]
        print(f"i={i}, j={j}, S={S}")
    return S


def PRGA(S, n):
    i = 0
    j = 0
    keystream = []

    print("\n=== PRGA ===")
    for step in range(n):
        i = (i + 1) % 10
        j = (j + S[i]) % 10

        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 10
        k = S[t]
        keystream.append(k)

        print(f"step={step+1}, i={i}, j={j}, t={t}, k={k}, S={S}")

    return keystream


def text_to_ascii(text):
    return [ord(c) for c in text]


def encrypt(plaintext, keystream):
    m = text_to_ascii(plaintext)
    c = []

    print("\n=== ENCRYPTION (XOR) ===")
    for i in range(len(m)):
        k = keystream[i]
        ci = m[i] ^ k   # XOR bitwise
        c.append(ci)

        print(f"{plaintext[i]}({m[i]}) XOR {k} = {ci}")

    return c


def to_ascii(cipher):
    return ''.join([chr(x) for x in cipher])


# ===== MAIN =====
plaintext = "cybersecurity"

S = KSA()
keystream = PRGA(S.copy(), len(plaintext))
cipher = encrypt(plaintext, keystream)
ascii_cipher = to_ascii(cipher)

print("\n=== RESULT ===")
print("Keystream:", keystream)
print("Cipher (decimal):", cipher)
print("Cipher (ASCII):", ascii_cipher)