#First, we need to import (bring in) the 'Fernet' tool from the cryptography library to use it.
from cryptography.fernet import Fernet
# This line creates a unique Secret Key that will be used for both locking and unlocking the message.
# Simply put, this is our private password for the encryption process.
key = Fernet.generate_key()
# Now, we create the actual 'cipher' object (the lock/unlock tool) and give it the 'key' it needs to operate.
cipher = Fernet(key)
#--- Encryption (Locking the Message) ---

# This is the original, readable message (Plaintext) that we want to protect.
message = "Hello, this is a secret message."
# We must convert the normal text (string) into 'bytes' because computers encrypt data in byte format Think of it as preparing the message for the locking mechanism.
encoded_message = message.encode()
# This is the main action: we use the 'cipher' tool to lock (encrypt) the message bytes.
encrypted = cipher.encrypt(encoded_message)
# We print the result. The 'b' prefix shows it's a byte string (the unreadable Ciphertext).
print("Encrypted message:", encrypted)

# --- Decryption (Unlocking the Message) ---

# We use the same 'cipher' tool to unlock (decrypt) the ciphertext.
# This only works because the 'cipher' object already holds the correct 'key'.
decrypted_bytes = cipher.decrypt(encrypted)

# Since the result is still in bytes, we must convert it back to readable text (string) using .decode().
decrypted = decrypted_bytes.decode()

# The final step: printing the original, unlocked message!
print("Decrypted message:", decrypted)
