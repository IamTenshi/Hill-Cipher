# Hill Cipher Implementation

This Python project implements the Hill Cipher encryption and decryption algorithm. The Hill Cipher is a polygraphic substitution cipher based on linear algebra, designed to encrypt and decrypt messages by using matrices.

## Overview

The project consists of two main files:

- `hill.py`: Contains the implementation of the Hill Cipher algorithm, including functions for encryption, decryption, and key handling.
- `main.py`: A demonstration script that showcases the usage of the Hill Cipher implementation with different keys and plaintexts.

## Usage

To run the demonstration script, use the following command:

```bash
$ python main.py
```



This will execute the script, demonstrating the encryption and decryption process with different keys and plaintexts.

## Files
hill.py: Contains the Hill Cipher implementation.
main.py: Demonstration script utilizing the Hill Cipher implementation.
LICENSE: The license information for this project.
Dependencies
NumPy: This project relies on NumPy for numerical operations and linear algebra.
You can install NumPy using the following command:

bash
Copy code
$ pip install numpy
Key Considerations
The MatrixNotInvertible exception is raised when attempting to use a non-invertible matrix as a key.

Ensure that your keys are square matrices to use the Hill Cipher algorithm.

License
This project is licensed under the MIT License.

Feel free to customize this README to include more details about your project, dependencies, and any specific instructions for users.

Happy encrypting and decrypting!
