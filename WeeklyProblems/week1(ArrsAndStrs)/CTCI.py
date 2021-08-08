'''
(CTCI 1.1) Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''
'''
# sort the string, iterate through each char and check neighboring char
def is_unique_chars(string):
    unique = True

    for i in range(len(string) - 1): # looping through: n
        if string[i] == string[i + 1]:
            unique = False

    return unique
'''

# make a list of booleans (initially False) where index corresponds to ASCII values
# then iterate through each char and check if that ASVII value has already been seen in the string (True)

def isUniqueChars(string):
    unique_bools = [False for i in range(256)]  # make a list of boolean values; ASCII values
    is_unique = True

    for c in string:
        if unique_bools[ord(c)] == False:
            # char's corresponding ASCII value is now taken
            unique_bools[ord(c)] = True

        else:
            # found a duplicate char
            is_unique = False
    
    return is_unique

'''1.2: Check permutation: Given two strings, write a method to check if one is a permutation of the other'''
def arePermutations(string1, string2):
    are_perms = True
    chars_table = [0 for char in range(256)]

    if (len(string1) != len(string2)):
        are_perms = False
    
    for c in string1:
        chars_table[ord(c)] += 1
    
    for c in string2:
        chars_table[ord(c)] -= 1
        if (chars_table[ord(c)] < 0):
            are_perms = False

    return are_perms 

'''1.3: URLify; Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space
at the end to hold the additinoal characters, and that you are given the true length of the string. 
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
'''
def turnURL(spaceStr, trueLen):
    spaces = 0
    fakeLen = 0

    for s in range(trueLen):
        # count number of spaces
        if spaceStr[s] == ' ':
            spaces += 1

    spaces *= 2
    fakeLen = (trueLen + spaces) - 1   # length of the string with adjustments to move chars

    for i in range(trueLen - 1, 0, -1):
        if spaceStr[i] == ' ':
            spaceStr[fakeLen] = '0'
            spaceStr[fakeLen - 1] = '2'
            spaceStr[fakeLen - 2] =  '%'
            fakeLen -= 3

        else:
            spaceStr[fakeLen] = spaceStr[i]
            fakeLen -= 1
    
    print(spaceStr)

# test_str = "Geo  Hotz    "
# turn_URL(list(test_str), 9) 

'''1.4: Palindrome Permutation; Given a string, write a function to check if it is a permutation of a palindrome. The palindrome does not need to be limited
to just dictionary words
Input: Tact Coa
Output: True (perms: "taco cat", "atco cta", etc.)
'''
def palinPerm(stringy):
    is_palinPerm = True
    char_map = {}
    num_odds = 0

    for c in stringy:
        if c != ' ':
            if c not in char_map:
                char_map[c] = 1
            
            else:
                char_map[c] += 1
    
    for key in char_map:
        # move through dict to check for num of odds 
        if char_map[key] % 2 != 0:
            # character has odd # of matches
            num_odds += 1

    if num_odds > 1:
        is_palinPerm = False
    
    return is_palinPerm

# print(palinPerm("tact coa"))

'''1.5: One Away; There are three types of edits that can be performed on strings: insert a char, remove a char, replace a char. Given two strings, write a function
to check if they are one edit (or zero edits) away.
Ex.: pale, ple --> True
pales, pale --> True
pale, bale --> True
pale, bake --> False
'''
def oneAway (string1, string2):
    chars_map = {c: 1 for c in string1} # initialize string1 hash table
    is_oneAway = True
    diff = 0    # num of chars different between the two strings

    if abs(len(string1) - len(string2)) > 1:
        # the lengths of the string must be the same or only one off from each other
        is_oneAway = False
    else:
        for c in string2:
            if c in chars_map:
                chars_map[c] += 1
        
        for matches in chars_map:
            if chars_map[matches] % 2 != 0:
                # at least one char has no other match
                diff += 1
            
            if diff > 1:
                is_oneAway = False
    
    return is_oneAway

# print(oneAway("pale", "bake"))

'''1.6: String Compression; Implement a method to perform basic string compression using the counts of repeated chars.
If the compressed string would not become smaller than the original string, your method should return the original string.
Assume the string only has upper/lower case letters (a-z=)
E.g.: 'aabcccccaaa' -> a2b1c5a3
'''
def strCompress(stringy):
    long_sets = 0
    curr_count = 1
    compressed = []

    for i in range(len(stringy) - 1):
        if stringy[i] == stringy[i + 1]:  
            curr_count += 1
            if curr_count > 2:
                # current substring is considered 'long' 
                long_sets += 1
        else:
            compressed.append(stringy[i])
            compressed.append(curr_count)
            curr_count = 1
    
    if (long_sets >= 1):
        # the compressed string is smaller than original string
        return ''.join(str(c) for c in compressed)
    
    return stringy

# print(strCompress("aabccccaaa"))

'''1.7: Matrix Rotation; Given an image represented by an N x N matrix, rotate the image (in-place) by 90 degrees
'''
def rotateMatrix(matrix):
    side_len = len(matrix)

    # Transpose the Matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # Switch the row and column indices
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for r in range(len(matrix)):
        for i in range(len(matrix[r]) // 2):
            # oppI is the opposing index to i
            oppI = side_len - 1 - i
            matrix[r][i], matrix[r][oppI] = matrix[r][oppI], matrix[r][i]
    
    return matrix
            
        
print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))

'''1.9: String Rotation; Assume you have a method isSubString which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using ONLY ONE call to isSubString.
E.g.: "waterbottle" is a rotation of "erbottlewat"
'''
class StringCompy:
    def __init__(self):
        pass

    def isSubStr(self, s1, s2):
        isSub = False
        matches = 0

        for c in range(len(s1) - len(s2) + 1):  # O(n)
            # move through s1 until it's impossible to have a substring
            for i in range(len(s2)):  
                if s1[c + i] == s2[i]:
                    matches += 1

            if matches == len(s2):
                # the substring is found
                isSub = True
        
        return isSub
    
    def isStringRot(self, s1, s2):
        '''wat|erbottle --> erbottlewat'''
        isRotated = False
        rot_len = 0
        temp_str = []
        
        if len(s1) != len(s2):
            return isRotated

        if s1 == "" and s2 == "":
            return True

        for i in range(len(s1)):
            # O(n)
            if s1[i] == s2[0]:
                # potentially found the breakoff point
                for c in range(len(s1) - rot_len):
                    # add every char into list after the breakoff point
                    temp_str.append(s1[i + c])
                break
            rot_len += 1
        
        sub_str = ''.join(temp_str)

        if len(sub_str) == 0:
            return isRotated

        if self.isSubStr(s2, sub_str):
            isRotated = True
        
        return isRotated


# stringer = StringCompy()
# print(stringer.isStringRot("", ""))

