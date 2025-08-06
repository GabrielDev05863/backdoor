#hashes generator sha256

import hashlib

def generate_sha256_hash(input_string):
    sha256_hash = hashlib.sha256(input_string.encode())
    return sha256_hash.hexdigest()

#test the function

input_string = input("typing the string to hash: ")
hash_result = generate_sha256_hash(input_string)
print(f"The hash sha256 of '{input_string}' is: {hash_result}") 