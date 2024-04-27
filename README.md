# Python_Caesar-Cipher-Encryption-and-Decryption
Python based Encryption and Decryption.

**Caesar Cipher Encryption and Decryption**

This Python script implements a Caesar cipher for basic text encryption and decryption. It allows users to encrypt or decrypt a message using a chosen shift value.

**Features:**

* **Encryption and Decryption:** Encrypts plain text using the Caesar cipher algorithm and decrypts encrypted messages.
* **User Interaction:** Provides a menu-driven interface for user input and interaction.

**Getting Started**

1. **Save the Code:** Save the code as a Python file (e.g., `caesar_cipher.py`).
2. **Run the Script:** Execute the script from the command line using `python caesar_cipher.py`.

**Usage**

The script presents a menu with the following options:

1. **Encrypt the Text:** Prompts the user to enter a message and a shift value. It then encrypts the message using the Caesar cipher and displays the encrypted text.
2. **Decrypt the Text:** Prompts the user to enter an encrypted message and a shift value. It then decrypts the message using the Caesar cipher and displays the decrypted text.

**Example Usage:**

```
Welcome to Encryption & Decryption using
        subtution Techniques of ceaser cypher

1. Encrypt the Text
2. Decrypt the Text

Enter your Option : 1

Ready To Encrypt

enter string: hello world
enter shift number: 3

After Encryption: khoor zruog
```

**How it Works**

The Caesar cipher is a simple substitution cipher where each letter in the message is shifted a certain number of positions down (or up) the alphabet. This code implements the Caesar cipher algorithm for both encryption and decryption.

**Improvements**

* **Error Handling:** Consider adding error handling for invalid user input (e.g., non-numeric shift values, invalid characters in the message).
* **Modularization:** Refactor the code into separate functions for encryption, decryption, and user input, improving readability and maintainability.
* **Enhanced Security:**  Caesar cipher is a weak encryption method. For stronger security, explore more advanced encryption techniques.
* **Character Handling:** The current implementation doesn't handle punctuation symbols or characters outside the alphabet (uppercase and lowercase). You could extend it to handle these cases appropriately.

**License**

This code is provided under the MIT license. Feel free to use, modify, and distribute it as needed, with attribution to the original author.
