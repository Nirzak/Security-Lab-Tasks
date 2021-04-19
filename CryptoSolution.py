"""
Created on Mon Apr 19 20:36:57 2021

@author: NirZak
"""
from Crypto.Cipher import AES # Importing AES library
from Crypto.Random import get_random_bytes # Generating random keys for AES
from Crypto.Util.Padding import pad, unpad # For encryption/decryption using AES
from Crypto.PublicKey import RSA #Importing RSA library
import Crypto.Signature.PKCS1_v1_5 as sign_PKCS1_v1_5 # For signature/Verify Signature
from Crypto.Cipher import PKCS1_v1_5 # For encryption/decryption using RSA
from Crypto import Random
from Crypto.Hash import SHA256
import time # Timer function

def rsacrypto(input_file, output_file, key_size):
    start = time.time()
    print("Generating Key Pair...")
    key_pair = RSA.generate(key_size) # Generating Key Pairs
    s_key = key_pair.export_key()  # Private key
    g_key = key_pair.publickey().export_key()  # Public key

    #Writing keys into a file
    with open("c.pem", "wb") as x:
         x.write(s_key)
    with open("d.pem", "wb") as x:
         x.write(g_key)

    # Input the original file
    file_in = open(input_file, "rb")  # opening for reading as binary
    data = file_in.read()
    text = data.decode("latin-1")
    print("Original Text from the File:", text)
    file_in.close()

    # Encryption Process
    print("Encryption Started...")
    encryptor = PKCS1_v1_5.new(RSA.importKey(g_key))
    ciphertext = encryptor.encrypt(text.encode())
    file_out = open(output_file, "wb")  # Open file to write bytes
    file_out.write(ciphertext)  # Writing encrypted data to the file
    file_out.close()
    print("Encrypted file saved as ", output_file)

    # Input the ciphertext from cipher file
    print("Decryption Started...")
    print("Loading Encrypted file")
    file_in = open(output_file, 'rb')  # Open the file to read bytes
    ciphered_data = file_in.read()  # Read the rest of the data
    file_in.close()
    #ciphered_data = ciphered_data.decode("latin-1")
    decryptor = PKCS1_v1_5.new(RSA.importKey(s_key))
    byte_object = decryptor.decrypt(ciphered_data, Random.new().read)
    plaintext = byte_object.decode()
    #plaintext = decryptor.decrypt(ciphered_data.decode())
    print("Text After Decryption:", plaintext)
    end = time.time()
    print("Time Taken:", (end-start))

def rsasign(input_file, output_file, key_size):
    start = time.time()
    print("Generating Key Pair...")
    key_pair = RSA.generate(key_size) # Generating Key Pairs
    s_key = key_pair.export_key()  # Private key
    g_key = key_pair.publickey().export_key()  # Public key
    #Writing keys into a file
    with open("c.pem", "wb") as x:
         x.write(s_key)
    with open("d.pem", "wb") as x:
         x.write(g_key)

    # Input the original file
    print("Loading Original File")
    file_in = open(input_file, "rb")  # opening for reading as binary
    data = file_in.read()
    #text = data.decode("latin-1")
    file_in.close()

    # Private key signature generation
    signer = sign_PKCS1_v1_5.new(RSA.importKey(s_key))
    rand_hash = SHA256.new()
    rand_hash.update(data)
    signature = signer.sign(rand_hash)
    file_out = open(output_file, "wb")  # Open file to write bytes
    file_out.write(signature)  # Writing encrypted data to the file
    file_out.close()
    print("Signature Generated and saved to", output_file)

    # Public key verification
    print("Verification process started..")
    print("Loading signature from", output_file)
    # Input signature from the file
    file_in = open(output_file, "rb")  # opening for reading as binary
    sign = file_in.read()
    file_in.close()
    verifier = sign_PKCS1_v1_5.new(RSA.importKey(g_key))
    _rand_hash = SHA256.new()
    _rand_hash.update(data)
    verify = verifier.verify(_rand_hash, sign)
    if(verify == True):
        print("Signature Verified!")
    else:
        print("Signature doesn't match!")
    end = time.time()
    print("Time Taken: ", (end-start))

def sha256gen(input_file):
    start = time.time()
    # Input the original file
    print("Loading File")
    file_in = open(input_file, "rb")  # opening for reading as binary
    data = file_in.read()
    file_in.close()
    hash_obj = SHA256.new()
    hash_obj.update(data)
    print("Generated SHA256 hash: ", hash_obj.hexdigest())
    end = time.time()
    print("Time Taken:", (end-start))

def aescrypto(input_file, mode, output_file, key_size):
    start = time.time()
    print("Generating Key...")
    if(key_size== "256"):
        key = get_random_bytes(32) #Generating the key
    else:
        key = get_random_bytes(16)
    key_location = "my_key.bin" #location to store the key

    # Save key to the file
    file_out_key = open(key_location, "wb")
    file_out_key.write(key)
    file_out_key.close()
    print("Key has been saved to ", key_location)

    # Input the original file
    print("Loading original file")
    file_in = open(input_file, "rb")  # opening for reading as binary
    data = file_in.read()
    text = data.decode("utf-8") # Decoding the byte object to print the text
    print("Original Text from the File:", text)
    file_in.close()


    # Create cipher object and encrypt the data
    if(mode == "CFB"):
        print("Encryption Started...")
        cipher = AES.new(key, AES.MODE_CFB)  # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

        file_out = open(output_file, "wb") # Open file to write bytes
        file_out.write(cipher.iv)  # Write the iv to the output file (will be required for decryption)
        file_out.write(ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)
        file_out.close()
        print("File ecrypted and saved as", output_file)

        # Input the key from the file
        file_in_key = open(key_location, "rb")  # Read bytes
        key_from_file = file_in_key.read()  # This key should be the same
        file_in_key.close()
        assert key == key_from_file, "keys doesn't match"  # Matching the keys

        # Decrypting procress starts here
        # Read the data from the cipher file
        print("Decryption Started...")
        print("Loading ciphertext file")
        file_in = open(output_file, 'rb')  # Open the file to read bytes
        iv = file_in.read(16)  # Read the iv out - this is 16 bytes long
        ciphered_data = file_in.read()  # Read the rest of the data
        file_in.close()

        cipher = AES.new(key_from_file, AES.MODE_CFB, iv=iv)  # Setup cipher
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        original_data = original_data.decode("utf-8")
        print("Decrypted Text: ", original_data)
        end = time.time()
        print("Time Taken:", (end - start))
    else:
        print("Encrypting Started...")
        cipher = AES.new(key, AES.MODE_ECB)  # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

        file_out = open(output_file, "wb")  # Open file to write bytes
        file_out.write(ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)
        file_out.close()
        print("File ecrypted and saved as", output_file)

        # Input the key from the file
        file_in_key = open(key_location, "rb")  # Read bytes
        key_from_file = file_in_key.read()  # This key should be the same
        file_in_key.close()
        assert key == key_from_file, "keys doesn't match"  # Matching the keys

        # Decrypting procress starts here
        print("Decrypting Started...")
        print("Loading ciphertext file")
        file_in = open(output_file, 'rb')  # Open the file to read bytes
        ciphered_data = file_in.read()  # Read the rest of the data
        file_in.close()

        cipher = AES.new(key_from_file, AES.MODE_ECB)  # Setup cipher
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        original_data = original_data.decode("utf-8")
        print("Decrypted text: ", original_data)
        end = time.time()
        print("Time Taken:", (end - start))

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
    elif(choice == "2"):
        input_file = input("Type the path of the input file: ")
        output_file = input("Type the name of the output file (Eg. cipher.bin): ")
        key_size =  int(input("Type RSA Key Size in interger (eg. 2048): "))
        rsacrypto(input_file, output_file, key_size)
    elif(choice == "3"):
        input_file = input("Type the path of the input file: ")
        output_file = input("Type the name of the output file where signature will be stored: ")
        key_size =  int(input("Type RSA Key Size in interger (eg. 2048): "))
        rsasign(input_file, output_file, key_size)
    elif(choice == "4"):
        input_file = input("Type the path of the input file: ")
        sha256gen(input_file)
    else:
        print("please input correct choice!")
        main()


if __name__ == "__main__":
    main()