import base64
from json import loads

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def lambda_handler(event, context):
    private_key_base64 = "private_key_base64"
    encrypted_data = "encrypted_data"

    decrypted_data = decrypt_with_private_key(encrypted_data, private_key_base64)
    print("Decrypted Data:", decrypted_data)

def format_private_key(private_key_base64):
    private_key_pem = "-----BEGIN RSA PRIVATE KEY-----\n"
    private_key_pem += '\n'.join([private_key_base64[i:i + 64] for i in range(0, len(private_key_base64), 64)])
    private_key_pem += "\n-----END RSA PRIVATE KEY-----\n"
    return private_key_pem

def decrypt_with_private_key(encrypted_data, private_key_base64):
    private_key_pem = format_private_key(private_key_base64)
    private_key_sra = RSA.import_key(private_key_pem)
    cipher = PKCS1_OAEP.new(private_key_sra)
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    decrypted_data_bytes = cipher.decrypt(encrypted_data_bytes)
    response =  loads(decrypted_data_bytes.decode('utf-8'))

    return response

if __name__ == "__main__":
    lambda_handler(None, None)
