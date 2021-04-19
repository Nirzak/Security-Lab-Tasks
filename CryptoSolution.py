"""
Created on Mon Apr 19 20:36:57 2021

@author: NirZak
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aescrypto(input_file, mode, output_file, key_size):
    #Encryption process starts here
    if(key_size== "256"):
        key = get_random_bytes(32) #Generating the key
    else:
        key = get_random_bytes(16)
    key_location = "my_key.bin" #location to store the key

    print("the key is: ", key)

    #save key to the file
    file_out_key = open(key_location, "wb")
    file_out_key.write(key)
    file_out_key.close()

    #input the original file
    file_in = open(input_file, "rb")  # opening for reading as binary
    data = file_in.read()
    file_in.close()


    # Create cipher object and encrypt the data
    if(mode == "CFB"):
        cipher = AES.new(key, AES.MODE_CFB)  # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

        file_out = open(output_file, "wb") # Open file to write bytes
        file_out.write(cipher.iv)  # Write the iv to the output file (will be required for decryption)
        file_out.write(ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)
        file_out.close()

        # Input the key from the file
        file_in_key = open(key_location, "rb")  # Read bytes
        key_from_file = file_in_key.read()  # This key should be the same
        file_in_key.close()
        assert key == key_from_file, "keys doesn't match"  # Matching the keys

        # Decrypting procress starts here
        # Read the data from the cipher file
        file_in = open(output_file, 'rb')  # Open the file to read bytes
        iv = file_in.read(16)  # Read the iv out - this is 16 bytes long
        ciphered_data = file_in.read()  # Read the rest of the data
        file_in.close()

        cipher = AES.new(key_from_file, AES.MODE_CFB, iv=iv)  # Setup cipher
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        original_data = original_data.decode("utf-8")
        print(original_data)
    else:
        cipher = AES.new(key, AES.MODE_ECB)  # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

        file_out = open(output_file, "wb")  # Open file to write bytes
        file_out.write(ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)
        file_out.close()

        # Input the key from the file
        file_in_key = open(key_location, "rb")  # Read bytes
        key_from_file = file_in_key.read()  # This key should be the same
        file_in_key.close()
        assert key == key_from_file, "keys doesn't match"  # Matching the keys

        # Decrypting procress starts here
        file_in = open(output_file, 'rb')  # Open the file to read bytes
        ciphered_data = file_in.read()  # Read the rest of the data
        file_in.close()

        cipher = AES.new(key_from_file, AES.MODE_ECB)  # Setup cipher
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        original_data = original_data.decode("utf-8")
        print(original_data)

def main():

    print("Please Insert your Choice:\n1. AES Encryption-Decryption\n2. RSA Encryption-Decryption\n3. RSA Signature\n4. SHA-256 Hashing")
    choice = input()
    if(choice == "1"):
        input_file = input("Type the path of the input file: ")
        output_file = input("Type the name of the output file (Eg. cipher.bin): ")
        key_size = input("Type 128 for 128bit key 256 for 256 bit key: ")
        mode = input("Type the encryption-decrytion mode (Eg. ECB or CFB): ")
#        if(input_mode == "ECB"):
#            mode = "AES.MODE_ECB"
#        else:
#            mode = "AES.MODE_CBC"
        aescrypto(input_file, mode, output_file, key_size)


if __name__ == "__main__":
    main()