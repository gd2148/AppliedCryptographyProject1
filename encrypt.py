#!/usr/bin/python
import random

#randomly generate keyspace
#each letter has a set number of key values,
#which are randomly chosen distinct numbers between 0-105
def generateKeyspace():
    keyspace = {}
    for i in range(27):
        if i == 0:
            keyspace[' '] = []
        else:
            charkey = chr(i+96)
            keyspace[charkey] = []

    keyset = [i for i in range(106)]
    while len(keyset) > 0:
        if len(keyspace[' ']) < 19:
            charkey = ' '
        elif len(keyspace['a']) < 7:
            charkey = 'a'
        elif len(keyspace['b']) < 1:
            charkey = 'b'
        elif len(keyspace['c']) < 2:
            charkey = 'c'
        elif len(keyspace['d']) < 4:
            charkey = 'd'
        elif len(keyspace['e']) < 10:
            charkey = 'e'
        elif len(keyspace['f']) < 2:
            charkey = 'f'
        elif len(keyspace['g']) < 2:
            charkey = 'g'
        elif len(keyspace['h']) < 5:
            charkey = 'h'
        elif len(keyspace['i']) < 6:
            charkey = 'i'
        elif len(keyspace['j']) < 1:
            charkey = 'j'
        elif len(keyspace['k']) < 1:
            charkey = 'k'
        elif len(keyspace['l']) < 3:
            charkey = 'l'
        elif len(keyspace['m']) < 2:
            charkey = 'm'
        elif len(keyspace['n']) < 6:
            charkey = 'n'
        elif len(keyspace['o']) < 6:
            charkey = 'o'
        elif len(keyspace['p']) < 2:
            charkey = 'p'
        elif len(keyspace['q']) < 1:
            charkey = 'q'
        elif len(keyspace['r']) < 5:
            charkey = 'r'
        elif len(keyspace['s']) < 5:
            charkey = 's'
        elif len(keyspace['t']) < 7:
            charkey = 't'
        elif len(keyspace['u']) < 2:
            charkey = 'u'
        elif len(keyspace['v']) < 1:
            charkey = 'v'
        elif len(keyspace['w']) < 2:
            charkey = 'w'
        elif len(keyspace['x']) < 1:
            charkey = 'x'
        elif len(keyspace['y']) < 2:
            charkey = 'y'
        elif len(keyspace['z']) < 1:
            charkey = 'z'
        index = random.randrange(0,len(keyset))
        keyspace[charkey].append(keyset.pop(index))
    return keyspace

#encrypt plaintext using generated keyspace
#key value is chosen using a deterministic algorithm (j modulo key)
#j is the index of the character in the plaintext
def encryptPlaintext(inputStr, keyspace):
    ciphertext = ""
    for i in range(len(inputStr)):
        key = keyspace[inputStr[i]]
        keyIndex = i%len(key)
        cipherChar = key[keyIndex]
        ciphertext += str(cipherChar)
        if i != len(inputStr)-1:
            ciphertext += ','
    return(ciphertext)

keyspace = generateKeyspace()
inputStr = input('Plaintext to be encrypted:\n')
print("Ciphertext:")
print(encryptPlaintext(inputStr, keyspace))