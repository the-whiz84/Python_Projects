
# I. Authentication with Flask


# I.1. Encryption

Encryption scramble a piece of data with a secret key or algorithm. Then it can only be deciphered with that key.
Examples of early encryption: Caesar Cypher and the Enigma Machine.

# Encryption
# Password      Key         Cipher Method       Ciphertext
    qwerty       1          Caesar Cypher  -->     rvfsuz

# Decryption
# Password        Cipher Method     Key       Ciphertext
    qwerty  <--    Caesar Cypher     1         rvfsuz


# I.2 Hashing

Instead of using an encryption key that can be stolen or cracked, hashing removes it altogether.
We store the hash in our database instead of the cyphertext.

# Password      Hash Function       Hash
                    -->

# Hash Function uses mathematical operations that makes it almost impossible to decipher the data.
# When a user logs in, we turn the password into a hash using the same hash function and we compare the 2 hashes.


# II. Hacking Passwords 101

Adbobe got hacked in 2013 (38 million accounts leaked, 3 million credit card information).
LinkedIn got hacked in 2012 (167 million accounts leaked).

https://haveibeenpwned.com
# check if your email was involved in a leak

# Same password will always turn into the same hash, so reusing passwords will give hackers the same hash for multiple accounts.
# They use hash tables that have hashes for all the commonly used passwords for each hash function and compare them with the leaked hash.

# How to create a Hash Table
- all words from a dictionary (~150.000)
- all telephone numbers from a phone book (~5.000.000)
- all combinations of characters up to 6 places (19.770..609.664)

Together they resuslt in aprox 19.8 billion combinations.
Apart from these, very large Hash Tables have been created and are for sale that contain the most common passwords from these past hacks.

# How long does it take a modern PC to go through the table with a powerful GPU that is extremely good at parallel processing?
- 20 Billion MD5 Hashes/second !!!


# III. Salting Passwords
To prevent dictionary attacks or Hash tables crack, we use Salting

# Salting combines the user's password with a random set of characters and then turned into a Hash.

# Password  +   Salt    Hash Function       Hash
    qwerty     28891       -->              

# THe salt is something that the user doesn't need to remember and is stored in the DB with the hash

# Bcrypt is a standard hashing algorithm that developers use to keep user's data secure
- 20 Billion MD5 Hashes/second  - 3 sec hack vs
- 17.000 bcrypt Hashes/second - 8 months hack

# Bcrypt has something called Salt Rounds - how many rounds will you salt your password with

# Password  +   Salt    Hash Function       Hash
1.    qwerty    28891       -->            hash
2.      hash    28891       -->             new_hash
3.   new_hash   28891       -->             newer_hash 
# The numnber of times you repeat the process is the number of Salt Rounds


# When a user logs in, the systems takes the input password, combines it with the salt stored in the DB and runs it through the same number of salting rounds. It then compares the final hash with the hash stored in the DB.

