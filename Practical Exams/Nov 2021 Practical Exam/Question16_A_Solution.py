# Question 16(a)
# Student name: 

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1)== sorted(w2):
        return True
    else:
        return False
            
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ") #part (i)
word1 = word1.upper()
word2 = word2.upper() #part (iv)
            
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if(sorted(word1) == sorted(word2)):
    print(word1,"is an anagram of",word2) #part (ii)
else:
    print(word1,"is NOT an anagram of",word2) #part (iii)

#part (v)
result = is_anagram(word1,word2)
if result == True:
    print(word1,"is an anagram of",word2)
else:
    print(word1,"is NOT an anagram of",word2)

#part (vi)
phrase = input("Enter a phrase: ")
phrase = phrase.upper()
phrase_no_spaces = phrase.replace(' ','')

if(sorted(phrase_no_spaces) == sorted(word1)):
    print(phrase,"is an anagram of",word1)
else:
    print(phrase,"is NOT an anagram of",word1)
    
if(sorted(phrase_no_spaces) == sorted(word2)):
    print(phrase,"is an anagram of",word2)
else:
    print(phrase,"is NOT an anagram of",word2)