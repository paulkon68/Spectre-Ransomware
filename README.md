# Spectre-Ransomware
A ransomware C&amp;C server and client, project built during the postgraduate course of System Security of University of Thessaly, Computer Science and Biomedical Informatics, Lamia, Greece

### ***How does it Work?***

First of all when executed, the rclient.py encrypts all of the files of the "targets/" directory using a 32-bit symmetric key according the AES encryption algorithm. Subsequently, the symmetric key is encrypted using the RSA algorithm and the public key that exists as a variable inside the script.

When the transaction is completed, the encrypted symmetric key is decrypted by the rserver.py's private key and the encrypted files are restored.
