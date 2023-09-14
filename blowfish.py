import sys
import os


def permute_des_key(key):
    permuted_choice_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52,
                         44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    perm_key = ''
    for i in range(len(permuted_choice_1)):
        perm_key += key[permuted_choice_1[i]-1]
    return perm_key


def hex_to_bin(text) -> str:
    hex = ''
    for chr in text:
        hex += "{0:04b}".format(int(chr, 16))
    return hex


def get_text(file: str) -> str:
    with open(file, 'r') as f:
        text = f.read()
    return text


def des_encrypt(plaintext: str, key: str):
    pt_in_bin = hex_to_bin(plaintext)
    print(pt_in_bin)
    key = hex_to_bin(key)
    # key_split = [key[i:i+8] for i in range(0, len(key), 8)]
    print(key)
    key_perm = permute_des_key(key)
    print(key_perm)
    c0 = key_perm[:28]
    d0 = key_perm[28:]
    print(c0)
    print(d0)


def blowfish_encrypt(plaintext: str):
    pass


def blowfish_decrypt(ciphertext: str):
    pass


if len(sys.argv) < 6:
    print(
        "Usage: blowfish {function} {method} {key filename} {input filename} {output filename}", file=sys.stderr)
    sys.exit()

function = sys.argv[1]
method = sys.argv[2]
key_file = sys.argv[3]
input_file = sys.argv[4]
output_file = sys.argv[5]

if function.lower() == 'e' or function.lower() == 'encrypt':
    function = 'ENCRYPT'
elif function.lower() == 'd' or function.lower() == 'decrypt':
    function = 'DECRYPT'
else:
    print("Function must be 'encrypt' or 'decrypt'", file=sys.stderr)

if method.lower() == 'des':
    method = 'DES'
else:
    print("Function must be 'DES'", file=sys.stderr)

# does key file exist?
if not os.path.isfile(key_file):
    print(f"Input file not found: {key_file}", file=sys.stderr)

# does input file exist?
if not os.path.isfile(input_file):
    print(f"Input file not found: {input_file}", file=sys.stderr)

if function == "ENCRYPT":
    if method == "DES":
        ct = des_encrypt(get_text(input_file), get_text(key_file))
        print(ct)
