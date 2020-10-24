Key_To_Frequency_Mapping = {" ":19, "a":7, "b":1,"c":2,"d":4,"e":10,"f":2,"g":2,"h":5,"i":6,"j":1,"k":1,"l":3,"m":2,"n":6,"o":6,"p":2,"q":1,"r":5,"s":5,"t":7,"u":2,"v":1,"w":2,"x":1,"y":2,"z":1}

def read_dictionary1():
    candidate_plaintexts = []
    lines = open("test1_dictionary.txt").read().split("\n")
    count = 1
    for line in lines:
        if line != "Test 1" and line != "" and not line.startswith("Candidate Plaintext"):
            candidate_plaintexts.append(line)
    return candidate_plaintexts

def read_dictionary2():
    candidate_plaintexts = []
    lines = open("test2_dictionary.txt").read().split("\n")
    count = 1
    for line in lines:
        if line != "Test 2" and line != "":
            candidate_plaintexts.append(line)
    #print (candidate_plaintexts)
    return candidate_plaintexts



#Groups char based on their frequency
#Let's call this charFreq mapping
# { 
    # 1: ['b', 'k', 'j', 'q', 'v', 'x', 'z'], 
    # 2: ['c', 'g', 'f', 'm', 'p', 'u', 'w', 'y'], 
    # 3: ['l'], 
    # 4: ['d'], 
    # 5: ['h', 's', 'r'], 
    # 6: ['i', 'o', 'n'], 
    # 7: ['a', 't'], 
    # 10: ['e'], 
    # 19: [' ']}
def words_to_freq():
    char_to_freq = {}
    for x in range(1,20):
        for key in Key_To_Frequency_Mapping:
            if Key_To_Frequency_Mapping[key] == x:
                if x in char_to_freq:
                    char_to_freq[x].append(key)
                else:
                    char_to_freq[x] = []
                    char_to_freq[x].append(key)
    return char_to_freq

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


#Attempting to analyse number of occurence of char with 1 char occuring in a word
def analyseCandidatePlaintext(candidate_plaintext,ciphertext):
    print candidate_plaintext
    print ciphertext

    #Finds position of low freq char in candidate plaintexts
    char_to_freq = words_to_freq()
    freqPosMapping = {}

    for char in char_to_freq[1]:
        freqPosMapping[char] = findOccurrences(candidate_plaintext, char)

    print freqPosMapping

    #CompareCipherText  
    for char in freqPosMapping:
        if len(freqPosMapping[char]) != 0:
            #Get number in first pos
            charToCipherGuess = ciphertext[freqPosMapping[char][0]]
            for pos in freqPosMapping[char]:
                if ciphertext[pos] != charToCipherGuess:
                    print "Failed"
                    return False
    return True

dictionary1 = read_dictionary1()
dictionary2 = read_dictionary2()

dictionary1.insert(0,"cbcb gbgg gcb")
ciphertext = [98,23,11,23,79,34,23,56,34,82,34,11,23]

for candidate_plaintexts in dictionary1:
    found = analyseCandidatePlaintext(candidate_plaintexts,ciphertext)
    if found:
        print p
        break


#Left to do:
# 1. generateCandidatePlaintext
# 2. Neaten code (Add stdin & suggested output)
# 3. Proper testing