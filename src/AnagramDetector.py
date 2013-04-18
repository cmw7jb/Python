'''
Created on Apr 10, 2013

@author: Cameron
'''
"""
Takes in a filename to a while containing words and the word to compare them against
Determines if the entered word is an anagram to any of the words in the file
If so, prints out the word from the file
"""

#Sorts the word passed
def get_sorted_string(word):
    return "".join(sorted(word))


def print_anagrams():
    #Get the file name and make sure it is not empty
    file_name = str(raw_input("Enter the file name: "))
    while len(file_name) == 0:
        print "File name cannot be empty"
        file_name = str(raw_input("Enter the file name:"))
        
    #Try to open the file, if unable then stop the program
    try:
        with open(file_name): pass
    except IOError:
        print "Unable to open file"
        return
        
    #Get the comparison word and make sure it is not empty
    word = str(raw_input("Enter the word to compare to: "))
    while len(word) == 0:
        print "Comparison word cannot be empty"
        word = str(raw_input("Enter the word to compare to:"))
        
    #Remove and trailing whitespace
    word = word.rstrip()
    
    #Open the file for reading
    with open(file_name, "r") as my_file:
        #Go through each line in the file
        for line in my_file:
            #Convert the line to a string so we can do string operations on it
            line = str(line)
            #Get rid of the newline character at the end of the lines
            line = line.replace('\n', "")
            
            #Sort both the comparison string and the line
            #If they are equal, then they are anagrams
            if get_sorted_string(word) == get_sorted_string(line):
                print "Matched: ", line
                
if __name__ == "__main__":
    print_anagrams()
            
        
