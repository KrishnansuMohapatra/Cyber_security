from cryptography.fernet import Fernet


#Genrate a secret key
key=Fernet.generate_key()
#Create Fernet cipher
cipher=Fernet(key)

#Encrypt
with open("../Fernet/secret.txt", "rb")as file:
    original_data=file.read()
    encrypted_data=cipher.encrypt(original_data)
with open("../Fernet/secret.txt.encrypted", "wb")as file:
    file.write(encrypted_data)
print("🔐 File encrypted successfully")

#Decrypt
with open("../Fernet/secret.txt.encrypted", "rb") as file:
    encrypted_data=file.read()
    decrypted_data=cipher.decrypt(encrypted_data)
with open("../Fernet/secret_decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("🔓 File decrypted successfully.")

