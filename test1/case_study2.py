import re
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)


Reference_id = input("Enter your Reference_id - ")

if (re.fullmatch(r"[A-Za-z0-9$#@]{12}",Reference_id)):
	print("Valid Password")
else:
	print("Invalid password")

encrypt_reference_id = fernet.encrypt(Reference_id.encode())


print(encrypt_reference_id)

print("Press Y/y to decrypt the password")
a = input()
if (a == 'Y' or a == 'y'):
	decrypt_reference_id = fernet.decrypt(encrypt_reference_id).decode()
	print(decrypt_reference_id)

