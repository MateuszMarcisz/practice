cw = '''
Description:
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
'''

def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    for _ in range(n):
        mid_point = len(encrypted_text) // 2
        odds = encrypted_text[:mid_point]
        evens = encrypted_text[mid_point:]
        decrypted_text = ""

        for i in range(len(evens)):
            decrypted_text += evens[i]
            if i < len(odds):
                decrypted_text += odds[i]
        encrypted_text = decrypted_text

    return decrypted_text


def encrypt(text, n):
    if not text or n <= 0:
        return text
    encrypted_text = text
    for _ in range(n):
        encrypted_text = encrypted_text[1::2] + encrypted_text[::2]

    return encrypted_text


# print(encrypt("012345", 1))
# print(encrypt("012345", 2))
# print(encrypt("012345", 3))
# print(encrypt("01234", 1))
# print(encrypt("01234", 2))
# print(encrypt("01234", 3))
print(decrypt("This is a test!", 0))
print(decrypt("hsi  etTi sats!", 1))
print(decrypt("s eT ashi tist!", 2))
print(decrypt(" Tah itse sits!", 3))
print(decrypt("This is a test!", 4))