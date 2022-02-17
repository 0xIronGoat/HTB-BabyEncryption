def decryption(msg):
    # Define an empty array for the resulting plain text answer
    pt = []
    # For every byte in the encrypted msg, loop through all the 256 possible ASCII character codes (0 - 255)
    # And perform same calculation on that character as is done in the chall.py file
    for byte in msg:
        for char in range(256):
            encrypted_char = ((123 * char + 18) % 256)
            # If resulting encrypted_char is same as the byte in the message we're currently looking at
            # Then add char to the pt[] array
            if encrypted_char == byte:
                pt.append(chr(char))

    # Return the completed pt[] array which should now have a decrypted message
    return ''.join(pt)


# Set ct as the cipher text file
ct = open('./msg.enc', 'r')

# Convert hex contents of ct to raw bytes and store in ctBytes
ctBytes = bytes.fromhex(ct.read())

# Call the decryption function, passing it ctBytes
print(decryption(ctBytes))
