Key_To_Frequency_Mapping = {" ":19, "a":7, "b":1,"c":2,"d":4,"e":10,"f":2,"g":2,"h":5,"i":6,"j":1,"k":1,"l":3,"m":2,"n":6,"o":6,"p":2,"q":1,"r":5,"s":5,"t":7,"u":2,"v":1,"w":2,"x":1,"y":2,"z":1}


class project1Cryptanalysis:

    def __init__(self):
        ciphertext = str(raw_input("Enter Cipher Text: "))
        #ciphertext = open("t").read()
        #print ciphertext
        #Assuming it's a string like -> 98,23,11,23,79,34,23,56,34,82,34,11,23
        ciphertext = ciphertext.split(",")  #Coverted it to an array
       

        dictionary1 = self.read_dictionary1()

        for candidate_plaintext in dictionary1:
            found = self.analyseCandidatePlaintext(candidate_plaintext,ciphertext)
            if found:
                print "My plaintext guess is:", candidate_plaintext
                break
        
        
        if not found: #Move on to dictionary 2
            print "Checking Dictionary 2. Hang in there, this might take a while..."
            dictionary2 = self.read_dictionary2()
            
            candidate_plaintexts = self.generateCandidatePlaintexts(dictionary2)
            
            for candidate_plaintext in candidate_plaintexts:
                candidate_plaintext = " ".join(candidate_plaintext)[0:500]
                found = self.analyseCandidatePlaintext(candidate_plaintext,ciphertext)
                if found:
                    print "My plaintext guess is:", candidate_plaintext
                    break


    def read_dictionary1(self):
        candidate_plaintexts = []
        lines = open("test1_dictionary.txt").read().split("\n")
        count = 1
        for line in lines:
            if line != "Test 1" and line != "" and not line.startswith("Candidate Plaintext"):
                candidate_plaintexts.append(line)
        return candidate_plaintexts

    def read_dictionary2(self):
        candidate_plaintexts = []
        lines = open("test2_dictionary.txt").read().split("\n")
        count = 1
        for line in lines:
            if line != "Test 2" and line != "":
                candidate_plaintexts.append(line)
        #print (candidate_plaintexts)
        return candidate_plaintexts

    def generateCandidatePlaintexts(self, dictionary):
        return self.permute(dictionary)
        
    def permute(self, s):
        if len(s) == 0:
            return [[]]

        ret = [s[0:1] + x for x in self.permute(s[1:])]

        for i in range(1, len(s)):
            if s[i] == s[0]:
                continue
            s[0], s[i] = s[i], s[0]
            ret += [s[0:1] + x for x in self.permute(s[1:])]

        return ret

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
    def words_to_freq(self):
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

    def findOccurrences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]


    #Attempting to analyse number of occurence of char with 1 char occuring in a word
    def analyseCandidatePlaintext(self,candidate_plaintext,ciphertext):
        
        #Finds position of low freq char in candidate plaintexts
        char_to_freq = self.words_to_freq()
        freqPosMapping = {}

        for char in char_to_freq[1]:
            freqPosMapping[char] = self.findOccurrences(candidate_plaintext, char)


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

        

project1Cryptanalysis()

#Left to do:
# 1. generateCandidatePlaintext
# 2. Neaten code (Add stdin & suggested output)
# 3. Proper testing