# main.py

import numpy as np
from hill import *

def main():
    keys = [
        np.array([[7, 8], [11, 11]]),
        np.array([[5, 15], [4, 12]]),  # Wrong and not square
        np.array([[19, 8, 4], [3, 12, 7]]),  # Wrong
    ]

    plaintexts = ["ATTACKATDAWN", "ATTACKATDAWN", "ATTACKATDAWN"]
    modulus = 26

    for i, key in enumerate(keys):
        print(f"\n--- Input {i + 1} ---")

        try:
            # Check if the matrix is square
            if key.shape[0] != key.shape[1]:
                raise MatrixNotInvertible("The matrix is not square.")

            # Check if the matrix is invertible
            if invertible(key):
                print("Matrix Information:")
                print(f"Square Matrix: {key.shape[0]}x{key.shape[1]}")
                print("The matrix is invertible.")
            else:
                raise MatrixNotInvertible("The matrix is not invertible.")

            print("\nEncryption:")
            print("Plaintext:", plaintexts[i])
            encoded_plaintext = encode(plaintexts[i])
            print("Encoded Plaintext (Numeric):", encoded_plaintext)

            ciphertext = encrypt(encoded_plaintext, key)
            print("Ciphertext (Numeric):", ciphertext)
            print("Ciphertext (String):", ''.join([chr(char + ord('A')) for char in ciphertext]))

            print("\nDecryption:")
            decryption_key = get_decryption_key(key)
            decrypted_text = decrypt(ciphertext, key)
            print("Decrypted Plaintext (Numeric):", decrypted_text)
            print("Decrypted Plaintext (String):", decode(decrypted_text))

        except MatrixNotInvertible as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    main()