from cryptography.fernet import Fernet
key=Fernet.generate_key()
print(f"Key: {key}")
#Encryption object
cipher=Fernet(key)
#original message
message=b"Hello my name is Krishnansu"
#Encrypt
encrypted=cipher.encrypt(message)
print("Encrypted:",encrypted)
#Decrypt
decrypted=cipher.decrypt(encrypted)
print("Decrypted",decrypted)