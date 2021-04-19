"""
Created on Mon Apr 19 20:36:57 2021

@author: NirZak
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def main():
    key = get_random_bytes(32) #Generating the key
    key_location = "my_key.bin" #location to store the key

    #save key to the file
    file_out = open(key_location, "wb")
    file_out.write(key)
    file_out.close()



    # Later on ... (assume we no longer have the key)
    file_in = open(key_location, "rb")  # Read bytes
    key_from_file = file_in.read()  # This key should be the same
    file_in.close()
    print(key_from_file)



    assert key == key_from_file, "keys doesn't match" #Matching the keys


if __name__ == "__main__":
    main()