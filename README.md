# Enigma-Python package

## Available as PyEnigmatic in Pypi - https://pypi.org/project/PyEnigmatic/0.0.3/

This python package provides access to several encryption and hashing functions. It essentially allows the user to obtain hashes, keys and encrypted, as well as decrypted, text by exposing existing cryptographic ciphers and hashing algorithms. In addition to that, the API has three methods, which when given a certain number of parameters, provides the user with prime numbers of any length of bits.

I have used PyNaCl cryptographic library, a Python binding to libsodium (fork of the Networking and Cryptography library), for some of the methods which provide symmetric key encryption and hashing, and for Advanced Encryption Standard (AES), I used the implementation of AES encryption cipher (CBC mode) in Pycryptodome library

Currently, this package provides the following cryptographic algorithms-

- Vigener Cipher (Complete implementation on my own)
- Caesar Cipher (Complete implementation on my own)
- Symmetric Key Cipher of PyNacl library (uses XSAlsa20 stream cipher)
- Advanced Encryption Standard (CBC Mode) of PyCryptodom library
- RSA (Rivest–Shamir–Adleman) -- Assymetric Key Cipher (Complete implementation of RSA cryptosystem on my own, and I have made some changes along )
- Password Hashing -- using key-stretching algos like argon2, argon2i and scrypt from PyNaCl library
- Hashing using SHA 256 or SHA 512 as implemented in PyNaCl library
- Prime Number Retrieval Algorithms - using the PyCryptodom library

## Table of Contents

- [Inspiration](#inspire)
- [Installation](#installation)
- [Usage](#usage)
- [PyNacl Cryptography](#pynacl)
- [PyCryptodome](#pycrypto)
- [HRSA (Implementation of RSA that supports encryption/decryption of all characters with an ascii value greater than 31)](#rsa)
- [Hashing](#hashing)
- [Caesar Cipher](#caesar)
- [Vigenere Cipher](#vig)
- [Primes](#prime)
- [RSA Public and Private Keys](#keys)
- [Improvements](#improvements)
- [Disclaimer](#disclaimer)
- [Author](#author)

### Inspiration

<a name="inspire">

My first foray into the world of computer science was through the world of cryptography. To be more precise, the movie- The Imitation Game - initated my venture into this field. Ever since then, my interest gradually turned into a commitment to the subject of computer science. I have built this project to re-visit the world of cryptograhpy with a better skill-set and knowledge.


### Installation

<a name="installation">

#### pip install PyEnigmatic

![setup](https://user-images.githubusercontent.com/63330003/117552037-fcd87c00-b06a-11eb-9576-d14c37f37370.PNG)


## USAGE

### AES

![aes](https://user-images.githubusercontent.com/63330003/117552046-095cd480-b06b-11eb-8bb7-6d85449d02b2.PNG)

### Primes

![all primes](https://user-images.githubusercontent.com/63330003/117552049-0e218880-b06b-11eb-9d95-731414f6d31d.PNG)


### Hashing

![hash1](https://user-images.githubusercontent.com/63330003/117552055-1679c380-b06b-11eb-96da-d1ea3447a6eb.PNG)

![hash23](https://user-images.githubusercontent.com/63330003/117552057-1974b400-b06b-11eb-8bf0-77424ec7f10d.PNG)


### RSA KEys

![keys](https://user-images.githubusercontent.com/63330003/117552064-22fe1c00-b06b-11eb-9507-d40e93fe53c6.PNG)


### PyNacl Encryption (Symmetric)

![nacl](https://user-images.githubusercontent.com/63330003/117552077-36a98280-b06b-11eb-9e4a-84dc8a740210.PNG)


### HRSA

![rsa](https://user-images.githubusercontent.com/63330003/117552087-432ddb00-b06b-11eb-9165-518c40129f83.PNG)


### Caesar and Vigenere

![vs](https://user-images.githubusercontent.com/63330003/117552094-4cb74300-b06b-11eb-9c97-401a59f9f894.PNG)



<a name='usage'>

### PyNacl Cryptographic Algorithms

<a name = 'pynacl'>

PyNaCl is a Python binding to libsodium, which is a fork of the Networking and Cryptography library, and LibSodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more. These libraries have a stated goal of improving usability, security and speed. More importantly, it does not require the developer to decide which encryption technique to use, and thus largely takes away the stress of knowing the underlying of a cipher and it’s potential vulnerabilities, making the process of encrypting/decrypting data more seamless. To summarize, it prevents the user from doing cryptography in an insecure way.

It by default provides the most secured and resistant mode of encryption, (for both symmetric and asymmetric) along with the required padding. Currently, it stands as one of the best libraries for cryptography. For more info - https://pynacl.readthedocs.io/en/stable/

### PyNacl Symmetric Key Encryption and Decryption

Symmetric Key Encryption is analogous to a locking/unlocking a safe. With the given key, you can encrypt and decrypt the data to view the contents. The implementation of this encryption is done through pynacl secret key encryption library, which uses XSalsa20 stream cipher to perform the algorithm with the given key. The decryption is also done using the same cipher.

The key passed in the request body must be of 32 bytes and should be kept secret. It is the combination to your “safe” and anyone with this key will be able to decrypt the data, or encrypt new data. To add a layer of randomness, I added some changes to the way the key gets used for the encryption at the end.

### Encryption

#### nacl_secret_key_encrypt_text(key,text)

For the encryption, the user must call the method nacl_secret_key_encrypt_text(key,text) where the key passed in should be of 32 bytes

### Decryption

#### nacl_secret_key_decrypt_text(key, text)

Similarly, for the decryption the user must call the method nacl_secret_key_decrypt_text(key, text) where the key passed in should be of 32 bytes and the text has to be the encrypted text returned

### PyCryptodom

<a name = 'pycrypto'>

PyCryptodome is a self-contained Python package of low-level cryptographic primitives. PyCryptodome is a fork of PyCrypto. I have used pycrtodome to implement Advanced Standard Encryption ( CBC mode) , and for those who are unaware of the AES, it’s essentially a symmetric key encryption, which uses the given key and an initialization vector ( a 128 bit round key) followed by multiple rounds of permutation and substitution on a 4x4 block of array of bytes to generate the encrypted text. For more detailed explanation of AES, you can visit the link https://en.wikipedia.org/wiki/Advanced_Encryption_Standard

### Advanced Standard Encryption ( CBC mode)

### Encryption

#### AES_encrypt(key, message, mode="CBC")

For using AES, this method - AES_encrypt(key, message, mode="CBC") - needs to be called.
The key passed in must be either of 128 or 192 or 256 bits, and the key should be kept safe. The mode should be set to "CBC".

### Decryption

### Advanced Standard Encryption ( CBC mode)

#### AES_decrypt(key, info,mode="CBC")

For using AES decryption, this method - AES_decrypt(key, info,mode="CBC") - needs to be called. The key passed in should be the same as the one passed for encryption. The info here is the dict that gets returned from the AES_encrypt function, and the dict contains the initialization vector used for the encryption and the encrypted text.

### HRSA (Implementation of RSA)

<a name = 'rsa'>

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.

I implemented this algorithm completely on my own and added changes to the original encryption so that only two prime numbers whose products happen to be larger than 100 would work. However, to ensure the maximum security, its best to use prime numbers of length more than 128 bits and the more the better. To get such HUGE prime numbers, you can use the prime number retrieval methods of this Enigma library. More information about the methods is given below. The Algroithm works for all characters with an ASCII value greater than 31, including all alphanumeric characters.

The prime numbers p1 and p2 used to obtain the private and public key for encryption must have a product of greater than 100. For the encryption method, you must provide the pubic key along with the product of p1 and p2 (n in this case), and for decryption method, you have to put the private key along with the product of p1 and p2 (n in this case) in the request body.

### Encryption

#### hrsa_encrypted(message,public,n)

This method - hrsa_encrypted(message,public,n) - needs to be called to encrypt any text using hrsa.

### Decryption

#### hrsa_decrypted(cipher,private,n)

This method - hrsa_decrypted(cipher,private,n) - needs to be called to decrypt the encrypted text obtained from the function above.

### Hashing

<a name = 'hashing'>

Cryptographic secure hash functions are irreversible transforms of input data to a fixed length digest.

The standard properties of a cryptographic hash make these functions useful both for standalone usage as data integrity checkers, as well as black-box building blocks of other kind of algorithms and data structures.

The methods below use hashing algorithms from the PyNacl libaray, and hence are well tested and safe to use. To know more, you can visit the two links below -

https://pynacl.readthedocs.io/en/stable/hashing/
https://pynacl.readthedocs.io/en/stable/password_hashing/

### Normal Hashing

#### nacl_hashing(message, sha=256)

To use this method, you must specifiy the type of hash function (SHA - 256 or 512) you would like to use for the given message. The hash functions available are sha 256 and 512. To know more - https://en.wikipedia.org/wiki/SHA-2

### Password Hashing

#### get_password_hash(password, algo=None)

To use this method, you must specify the desired key stretching algorithm and the ones available are - argon2id, argon2i, scrypt. The algo parameter
takes in the name of the algorithm to be used.

### Password Hashing Verify

#### verify_password_hash(password, hash)

For using this method, you have to provide the password/text along with its corresponding hash, generated from the method password hashing ( right above) . If the hashing provided is of the password/text given in as parameter, then the method returns true, otherwise returns false.

### Caesar Cipher

<a name = 'caesar'>

Implemented the Caesar Cipher completely on my own, and exposed the algorithm with the following method below. It works on both positive and negative shift, and to use the method, you must provide the text to be encrypted and the shift to be used on the text.

### Encryption

#### caesar_encrypt(word, shift)

This method encrypts the message with the given Shift and Caesar Cipher

### Decryption

#### caesar_decrypt(cipher, shift)

This method decypts the message with the given Shift and Caesar Cipher.
The cipher paramater should be the encrypted text returned from the function above for encryption.

### Vigenere Cipher

<a name = 'vig'>

#### vigenere_encrypt(string, key)

#### vigenere_decrypt(string, key)

Implemented the Vigenere Cipher completely on my own, and exposed the algorithm with the methods above for encryption and decryption. It works on key of any length, and to use the method, you must provide the text to be encrypted and the key to be used on the text. Howevere, the cipher implemented works best with lowercase letters only.

### Prime Numbers

<a name = 'prime'>

The mere existence of prime numbers has always been a mystery to me, and at this point, I can quite confidently say whoever is reading this would be aware of the importance of prime numbers in cryptography. If you need a refresher on the definition of a prime number, it's a number larger than 1 that's divisible only by itself and 1. If I had to put it simply, modern encryption algorithms exploit the fact that we can easily take two large primes and multiply them together to get a new, super-large number, but that no computer yet created can take that super-large number and quickly figure out which two primes went into making it. Using this particular complexity, public key cryptography, such as RSA, use prime numbers to encrypt/decrypt data. To know more, you can visit the link - https://math.berkeley.edu/~kpmann/encryption.pdf Below, the following methods would allow you to retrieve large prime numbers quickly, and all you have to do is just provide the length of prime number ( length in bits). You can use these methods to generate large primes for RSA.

### Prime number generation using a unique ID

#### hrsa_prime(unique_id)

Generates a prime number of length k bits by extracting a unique value from the ID given as parameter. To look into the algorithm I used, you can view the source code in the eucild_prime.py file.

### Prime number generation using the desired length (n)

#### generate_prime(n)

Generates a prime number of n bits ( n of the parameter)

### List of k Prime number generation of specific lengths

#### generate_kprimes(k, start, end)

Generates a list of k (length of list) prime numbers, which contains one prime number of all lengths starting from 'start' (length of bits) bits to 'end' bits (length of bits) K must be equal to the value start-end+1 . To look into the algorithm I used, you can view the source code in the eucild_prime.py file.

### RSA Public and Private Keys

<a name = 'keys'>

Implemented the Extended Euclidean Algorithm, along with RSA cipher completely on my own to generate the desired public key and the corresponding private key. To look into the algorithm I used, you can view the source code in the keys.py and prime_euclid.py file.

### Public Key RSA

#### generate_public_key(prime1,prime2)

Computes and returns the public key for RSA cipher using the prime numbers p1 and p2. Product of p1 and p2 must be greater than 100 for the algorithm to work correctly.

### Private Key RSA

#### generate_private_key(e,prime1,prime2)

Computes and returns the private key for RSA cipher using the prime numbers p1,p2 and the public key e. Product of p1 and p2 must be greater than 100 for the algorithm to work correctly.

## Improvements

<a name = 'improvements'>

In the foreseeable future, I intend to add more cryptographic functions to this package.

## Disclaimer

<a name = 'disclaimer'>

I have built this project to explore and learn about the world of cryptography, with a renewed sense of curosity. Hence, it's made purely for learning purposes. However, anyone willing to use this API is more than welcome to do so. Thanks!

## Author

<a name = 'author'>

Hamza Yusuff - Email: hbyusuff@uwaterloo.ca
