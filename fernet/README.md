```markdown
# 🔐 Secure File Vault using Fernet

A beginner-friendly Python cybersecurity project that uses **Fernet symmetric encryption** to encrypt and decrypt files securely.

The project demonstrates how encryption works, how symmetric keys are managed, and how encrypted files can be protected from unauthorized access.

> **✨ Rich CLI Support:** The command-line interface also has a version built with the [`rich`](https://github.com/Textualize/rich) library, giving colorful, styled output (panels, colored prompts, and status messages) instead of plain text.

---

## 📌 Project Overview

The main goal of this project is to understand **symmetric encryption** through a practical file-encryption application.

The application allows the user to:

- Generate an encryption key
- Store the key locally
- Load the existing key on future runs
- Encrypt files
- Decrypt encrypted files
- Detect invalid or modified encrypted data
- Use a simple command-line interface

The project uses the `Fernet` implementation provided by the Python `cryptography` library.

---

# 🔑 What is Symmetric Encryption?

Symmetric encryption means that the **same secret key** is used for both encryption and decryption.

```text
Original File
     ↓
   🔑 Key
     ↓
  Encrypt
     ↓
Encrypted File
     ↓
   🔑 Same Key
     ↓
  Decrypt
     ↓
Original File
```

If the correct key is not available, the encrypted data cannot be successfully decrypted.

---

# 🧠 Why Fernet?

Fernet provides a high-level interface for authenticated symmetric encryption.

It allows us to:

```python
key = Fernet.generate_key()
```

create a secure key and then use it to encrypt and decrypt data.

Example:

```python
cipher = Fernet(key)

encrypted = cipher.encrypt(data)

decrypted = cipher.decrypt(encrypted)
```

Fernet also provides integrity/authentication protection, meaning that modified or invalid encrypted data will not successfully decrypt.

---

# 🚀 Project Versions

The project was developed progressively.

## V1 — Basic Fernet

Learned the fundamental encryption/decryption process:

```text
Message
   ↓
Encrypt
   ↓
Encrypted Data
   ↓
Decrypt
   ↓
Message
```

The same key is required for both operations.

---

## V2 — File Encryption

Instead of encrypting only a message, the project was extended to work with actual files.

```text
secret.txt
    ↓
Fernet Encryption
    ↓
secret.txt.encrypted
```

The encrypted file contains unreadable encrypted data.

---

## V3 — Key Management

A major problem with V2 was discovered:

```python
Fernet.generate_key()
```

creates a new key every time the program runs.

If a new key is generated every time:

```text
Run 1 → Key A → Encrypt
Run 2 → Key B → Cannot decrypt with Key B
```

Therefore, the project was changed to save the key.

```text
First Run
    ↓
No key exists
    ↓
Generate key
    ↓
Save secret.key

Future Run
    ↓
secret.key exists
    ↓
Load existing key
```

This introduced the important concept of **key management**.

---

# V4 — Secure File Vault CLI

The final version combines the previous concepts into a command-line application.

The user can choose:

```text
==============================
       🔐 SECURE VAULT
==============================
1. Encrypt file
2. Decrypt file
3. Exit
==============================
```

The application automatically loads the existing key or generates one if it does not exist.

---

# 🏗️ Architecture

```text
                    Secure File Vault
                           │
                           ↓
                  Key Management
                           │
                ┌──────────┴──────────┐
                ↓                     ↓
          Existing Key            No Key
                ↓                     ↓
           Load Key              Generate Key
                │                     │
                └──────────┬──────────┘
                           ↓
                      Fernet Cipher
                           │
                  ┌────────┴────────┐
                  ↓                 ↓
              Encrypt            Decrypt
                  ↓                 ↓
             .encrypted           File
```

---

# 📁 Project Structure

```text
fernet_secure_vault/
│
├── secure_vault.py
├── secret.key
├── secret.txt
├── secret.txt.encrypted
└── .gitignore
```

---

# ⚙️ Technologies Used

* Python
* Cryptography
* Fernet
* pathlib
* File I/O
* Command Line Interface
* Rich (optional, for styled CLI output)

---

# 📦 Installation

Install the required dependency:

```powershell
uv add cryptography
```

Or with pip:

```powershell
pip install cryptography
```

If using the Rich-based CLI version, also install:

```powershell
pip install rich
```

---

# ▶️ Running the Project

Run:

```powershell
uv run secure_vault.py
```

The application will display:

```text
==============================
       🔐 SECURE VAULT
==============================
1. Encrypt file
2. Decrypt file
3. Exit
==============================
Choose an option:
```

---

# 🔐 Encrypting a File

Select:

```text
1
```

Then enter a file name:

```text
Enter file to encrypt: secret.txt
```

The application creates:

```text
secret.txt.encrypted
```

Example:

```text
secret.txt
     ↓
   Encrypt
     ↓
secret.txt.encrypted
```

---

# 🔓 Decrypting a File

Select:

```text
2
```

Then enter:

```text
Enter encrypted file: secret.txt.encrypted
```

The application decrypts the file using the stored key.

If the encrypted file is:

```text
secret.txt.encrypted
```

the decrypted output becomes:

```text
secret.txt
```

---

# 🔑 Key Management

The encryption key is stored in:

```text
secret.key
```

The program checks whether the key already exists.

Conceptually:

```python
if KEY_FILE.exists():
    key = KEY_FILE.read_bytes()
else:
    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)
```

This prevents the program from generating a completely new key every time it starts.

---

# ⚠️ Key Loss

The encryption key is extremely important.

If the encrypted file exists but the original key is lost:

```text
secret.txt.encrypted
        +
     No key
        ↓
   ❌ Decryption fails
```

Therefore:

> Protecting the encryption key is just as important as protecting the encrypted data.

---

# 🛡️ Error Handling

The application handles situations such as:

### File does not exist

```text
❌ File not found.
```

### Invalid encryption key or modified data

```text
❌ Decryption failed.
The key may be incorrect or the file may have been modified.
```

### Invalid menu option

```text
❌ Invalid choice. Please select 1, 2, or 3.
```

---

# 🔬 Important Experiment

A useful experiment is:

1. Encrypt a file.
2. Close the program.
3. Start the program again.
4. Decrypt the encrypted file.

It should work because the same `secret.key` is loaded.

Then:

1. Delete `secret.key`.
2. Keep the encrypted file.
3. Try to decrypt it.

The original encrypted file should no longer be decryptable with a newly generated key.

This demonstrates the importance of **key persistence and key management**.

---

# 🔒 Security Considerations

The `secret.key` file contains the encryption key.

It should **never be committed to GitHub**.

The project therefore uses:

```text
.gitignore
```

with:

```text
secret.key
*.encrypted
__pycache__/
.venv/
```

Do not publish the real encryption key with the project.

---

# 🧠 What I Learned

This project helped me understand:

### Python

* Functions
* File handling
* Binary files
* `Path`
* Exception handling
* CLI menus
* Working with external libraries

### Cryptography

* Encryption
* Decryption
* Symmetric encryption
* Secret keys
* Key generation
* Key persistence
* Key management
* Integrity/authentication

### Software Design

* Separating key management from encryption
* Separating encryption and decryption functions
* Input validation
* Error handling
* Reusable functions

---

# 🎯 Core Concept

The most important lesson from this project is:

```text
Encryption protects the data.
The key protects the ability to decrypt the data.
```

The encrypted file can be safely unreadable, but losing the key can mean losing access to the original data.

---

# 🚧 Limitations

This project is primarily an **educational cybersecurity project**.

It is not intended to be a complete production-grade secure storage system.

Some areas that would require additional engineering in a production application include:

* Secure key storage
* Key rotation
* Access control
* Key backup and recovery
* Secure deletion
* Authentication
* Multi-user support
* Audit logging
* Large-file handling
* Threat modeling

---

# 🔮 Possible Future Improvements

Possible extensions include:

* Password-based key derivation
* Password-protected vault
* Secure key management
* GUI interface
* Streamlit interface
* Drag-and-drop file encryption
* Folder encryption
* File integrity verification
* Key rotation
* Multi-file encryption
* Encrypted metadata
* Cloud storage integration

These features should be added only when there is a genuine requirement.

---

# 💡 Project Learning Path

```text
V1
Basic Fernet
   ↓
Understand encryption

V2
File Encryption
   ↓
Work with binary files

V3
Key Management
   ↓
Understand persistent encryption keys

V4
Secure File Vault
   ↓
Combine everything into a usable CLI
```

---

# 👨‍💻 Author

**Krishnansu Mohapatra**

MCA Graduate | Python | Machine Learning | AI | Data Analytics | Cybersecurity

---

# ⭐ Final Takeaway

This project started with a simple question:

> How can Python protect information from being readable by unauthorized people?

The answer introduced the concepts of:

```text
Plaintext
    ↓
Encryption
    ↓
Secret Key
    ↓
Ciphertext
    ↓
Secret Key
    ↓
Decryption
    ↓
Plaintext
```

The project demonstrates that implementing encryption is only part of the problem.

**Managing and protecting the encryption key is equally important.**
```