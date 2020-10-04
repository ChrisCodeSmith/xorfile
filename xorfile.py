#! python3
import sys
import getpass
import argparse
from os import path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="xor the content of a file")
    parser.add_argument("infile", help="file that you want to xor")
    parser.add_argument("--out", help="use this argument if you want to write" +
                        " to a different file then where you read")
    args = parser.parse_args()
    if path.exists(args.infile):
        input_filename = args.infile
    else:
        print(f"[*] file does not exist")
        sys.exit()
    if args.out:
        output_filename = args.out
    else:
        output_filename = input_filename
    # ---------- END Argument Parsing ---------------------------- #

    key = getpass.getpass()

    print(f"[*] reading input file ...")
    with open(input_filename, "rb") as file:
        data = file.read()
    output = bytearray()

    print(f"[*] processing ...")
    for i in range(0, len(data)):
        output.append(data[i] ^ ord(key[i % len(key)]))

    print(f"[*] writing outputfile ..")
    with open(output_filename, "wb") as file:
        file.write(output)
    print(f"[*] DONE - xor successfully written into {output_filename}.")
