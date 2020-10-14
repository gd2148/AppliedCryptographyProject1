#!/usr/bin/python
import random

def generateKey():
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
        index = random.randrange(0,len(keyset))
        keyspace[charkey].append(keyset.pop(index))


generateKey()