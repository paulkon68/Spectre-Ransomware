from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Generates the private RSA key, the public RSA key and writes them to the files: "key.pem" ans "pkey.key"
# respectively.

def generate_private_key():

    private_key = rsa.generate_private_key(

        public_exponent=65537,

        key_size=4096,

    )

    pem = private_key.private_bytes(

        encoding=serialization.Encoding.PEM,

        format=serialization.PrivateFormat.PKCS8,

        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')

    )

    with open("key.pem", "wb") as key_file:
        key_file.write(pem)

    public_key = private_key.public_key()
    pem = public_key.public_bytes(

        encoding=serialization.Encoding.PEM,

        format=serialization.PublicFormat.SubjectPublicKeyInfo

    )

    with open("pkey.key", "wb") as pk:
        pk.write(pem)


generate_private_key()
