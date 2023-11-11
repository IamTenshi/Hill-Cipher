# hill.py

import numpy as np

class MatrixNotInvertible(Exception):
    pass

def determinant(key_matrix):
    return np.linalg.det(key_matrix)

def invertible(key_matrix):
    return determinant(key_matrix) != 0

def mod_inverse(determinant, modulus):
    for i in range(1, modulus):
        if (determinant * i) % modulus == 1:
            return i
    return None

def encode(str_):
    return [ord(char) - ord('A') for char in str_]

def decode(arr):
    return ''.join([chr(char + ord('A')) for char in arr])

def encrypt(plaintext, key):
    num_cols = len(key[0])
    chunked_plaintext = [plaintext[i:i + num_cols] for i in range(0, len(plaintext), num_cols)]
    encrypted_chunks = []

    for chunk in chunked_plaintext:
        encrypted_chunk = (np.dot(key, np.array(chunk)) % 26).tolist()
        encrypted_chunks.extend(encrypted_chunk)

    return encrypted_chunks

def get_decryption_key(key):
    determinant_inv = mod_inverse(int(round(determinant(key))), 26)
    if determinant_inv is None:
        raise MatrixNotInvertible("The matrix is not invertible. The determinant is 0.")

    adjugate = np.round(np.linalg.inv(key) * determinant(key))
    decryption_key = (adjugate * determinant_inv) % 26
    return decryption_key.astype(int)

def decrypt(ciphertext, key):
    num_cols = len(key[0])
    decrypted_chunks = []

    for i in range(0, len(ciphertext), num_cols):
        chunk = ciphertext[i:i + num_cols]
        decrypted_chunk = (np.dot(get_decryption_key(key), np.array(chunk)) % 26).tolist()
        decrypted_chunks.extend(decrypted_chunk)

    return decrypted_chunks