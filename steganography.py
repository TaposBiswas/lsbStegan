#!/usr/bin/python3

import argparse
import sys
import random
import re

def embed_message(image_file, message, password):
    if not image_file.endswith(".png"):
        print("[-] Enter a .png file")
        sys.exit(1)

    if password == "no_password_given":
        password = "no_password_given"
    embedded_message = password + " " + message
    secret_image = lsb.hide(image_file, embedded_message)
    random_number = random.randint(0, 100)
    filename = "secret" + str(random_number) + ".png"
    secret_image.save(filename)
    print("File Saved as ", filename)

def reveal_message(image_file, password):
    if not password:
        print("[-] Enter a password")
        sys.exit(1)

    message = lsb.reveal(image_file)
    if re.findall(f'\\b{password}\\b', message):
        message = message.replace(password, "")
        print("The secret Message is ", message)
    else:
        print("Couldn't reveal the Message with the Passcode.")

def main():
    parser = argparse.ArgumentParser(description="Image Steganography\n[+] Use .png files only")
    parser.add_argument('-e', type=str, help="To embed a message in the image")
    parser.add_argument('-f', help="To pass .png (Image) file")
    parser.add_argument('-x', help="To extract the message from the image.", action="store_true")
    parser.add_argument('-p', help="To put in a password.", nargs="?", const="no_password_given")
    args = parser.parse_args()

    if args.f and args.e:
        embed_message(args.f, args.e, args.p)
    elif args.f and args.x:
        reveal_message(args.f, args.p)
    else:
        print("[-]Error Occured")
        print("[*]Try Again with the correct syntax.")
        print("[*]If you are trying to embed a message, try -e flag.")
        print("[*]If you are trying to extract a message then try -x flag")

if __name__ == "__main__":
    main()
