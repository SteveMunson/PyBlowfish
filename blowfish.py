import sys
import os


def blowfish(*args):
    print(args)


if len(sys.argv) < 5:
    print(
        "Usage: blowfish {function} {key filename} {input filename} {output filename}", file=sys.stderr)
    sys.exit()

function = sys.argv[1]
key_file = sys.argv[2]
input_file = sys.argv[3]
output_file = sys.argv[4]

if function.lower() == 'e' or function.lower() == 'encrypt':
    function = 'ENCRYPT'
elif function.lower() == 'd' or function.lower() == 'decrypt':
    function = 'DECRYPT'
else:
    print("Function must be 'encrypt' or 'decrypt'", file=sys.stderr)

# does key file exist?
if not os.path.isfile(key_file):
    print(f"Input file not found: {key_file}", file=sys.stderr)

# does input file exist?
if not os.path.isfile(input_file):
    print(f"Input file not found: {input_file}", file=sys.stderr)
