# Spectre-Ransomware
A ransomware C&amp;C server and client, project built during the postgraduate course of System Security of University of Thessaly, Computer Science and Biomedical Informatics, Lamia, Greece

### Usage

First, rserver.py must be run on the attacker's machine. ($python3 ./rserver.py). The rclient.py creates a GUI that represents the ransomware and encrypts the user files. For security reasons, there should be a targets/ directory with random files for the ransomware (rclient.py) to encrypt

### ***How does it Work?***

First of all when executed, the rclient.py encrypts all of the files of the "targets/" directory using a 32-bit symmetric key according the AES encryption algorithm. Subsequently, the symmetric key is encrypted using the RSA algorithm and the public key that exists as a variable inside the script.

When the transaction is complete, the encrypted symmetric key is decrypted by the rserver.py's private key and the encrypted files are restored.
The transaction can be completed with the pay_ransom.py script that sends the asked amount of bitcoins to the attacker.


![image](https://user-images.githubusercontent.com/66385713/183637288-18d306a4-b316-4ba7-8b27-90ab1552def7.png)
