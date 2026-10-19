

from cryptography.fernet import Fernet
from pathlib import Path


def generate_key(filename="secret.key"):
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print(filename)
    return key


def load_key(filename="secret.key"):
    with open(filename, "rb") as file:
        return file.read()


def check_file(filename="secret.key"):
    KEY_FILE = Path(filename)

    if KEY_FILE.exists():
        key = KEY_FILE.read_bytes()
        print("🔑 Existing key loaded.")
    else:
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        print("🔑 New key generated and saved.")

    cipher = Fernet(key)  # now built in both branches
    return cipher


def encrypt(filename, cipher):
    with open(filename, "rb") as file:
        data = file.read()

    encrypted = cipher.encrypt(data)

    out_path = filename + ".encrypted"
    with open(out_path, "wb") as file:
        file.write(encrypted)

    print("🔐 File encrypted.")
    return encrypted


def decrypt(filename, cipher, output_filename="secret_decrypted.txt"):
    with open(filename, "rb") as file:
        encrypted = file.read()

    decrypted = cipher.decrypt(encrypted)

    with open(output_filename, "wb") as file:
        file.write(decrypted)

    print("🔓 File decrypted successfully.")
    return output_filename


if __name__ == "__main__":
    cipher = check_file()

    demo = "demo.txt"
    with open(demo, "w") as f:
        f.write("hello world")

    encrypt(demo, cipher)
    decrypt(demo + ".encrypted", cipher)