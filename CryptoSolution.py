"""
Created on Mon Apr 19 20:36:57 2021

@author: NirZak
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def main():
    key = get_random_bytes(32) #Generating the key
    key_location = "my_key.bin" #location to store the key

    #save key to the file
    file_out_key = open(key_location, "wb")
    file_out_key.write(key)
    file_out_key.close()

    output_file = 'encrypted.bin'  # Output file
    input_file = open("test.txt", "rb")  # opening for reading as binary
    data = input_file.read()
    input_file.close()

    # Create cipher object and encrypt the data
    cipher = AES.new(key, AES.MODE_CBC)  # Create a AES cipher object with the key using the mode CBC
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

    file_out = open(output_file, "wb")  # Open file to write bytes
    file_out.write(cipher.iv)  # Write the iv to the output file (will be required for decryption)
    file_out.write(ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.close()

    # Later on ... (assume we no longer have the key)
    file_in_key = open(key_location, "rb")  # Read bytes
    key_from_file = file_in_key.read()  # This key should be the same
    file_in_key.close()
    #print(key_from_file)

    # Read the data from the file
    file_in = open("encrypted.bin", 'rb')  # Open the file to read bytes
    iv = file_in.read(16)  # Read the iv out - this is 16 bytes long
    ciphered_data = file_in.read()  # Read the rest of the data
    file_in.close()

    cipher = AES.new(key_from_file, AES.MODE_CBC, iv=iv)  # Setup cipher
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    original_data = original_data.decode("utf-8")
    print(original_data)


    #assert key == key_from_file, "keys doesn't match" #Matching the keys


if __name__ == "__main__":
    main()