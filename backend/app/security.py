from cryptography.fernet import Fernet
from passlib.context import CryptContext

# 1. Setup for Password Hashing
# We use bcrypt, which is a gold standard for passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 2. Setup for Data Encryption (Fernet)
# In a real app, this key would be stored in a secret environment variable
# For now, we generate one.
# WARNING: If you lose this key, you lose access to all encrypted data!
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_content(content: str):
    return cipher_suite.encrypt(content.encode()).decode()

def decrypt_content(encrypted_content: str):
    return cipher_suite.decrypt(encrypted_content.encode()).decode()