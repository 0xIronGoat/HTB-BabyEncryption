# HTB-BabyEncryption
This is a solution for the Hack The Box cryptography challenge Baby Encryption.  

I figured there's not a way to reverse the algorithm used to encrypt the message, so I took a brute force approach.

This script will loop through every character in `msg.enc`. For each one, it will then cycle through all possible ASCII characters and perform the same encryption as is seen in `chall.py`.
If it gets a match, then it adds it to the plain text output and, at the end, you will get the decrypted message.