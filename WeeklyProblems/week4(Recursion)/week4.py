'''Implement a regular expression-like pattern matcher. Given a "pattern" string 
you should be able to determine if an input string matches that pattern.
Pattern will be a string where each charcter in the string is either:
- A character from A-Z. In this case, match that char.
- A '.' character. In this case, match any single input character
- A '*' character. In this case, match 0 or more instances of the previous character in the pattern.
'''
def isMatch(pattern, string):

    if (not pattern and not string):
        # pattern and string are empty
        return True

    elif (not pattern):
        # pattern is not filled, string is filled
        return False

    else:
        # recurse
        if ('*' in pattern[0:2]):
            while (len(string) > 0 and pattern[0] == string[0]):
                string = string[1:]
            return isMatch(pattern[2:], string)    

        elif (len(string) > 0 and pattern[0] == string[0]):
            return isMatch(pattern[1:], string[1:])
        
        elif (len(string) > 0 and pattern[0] == '.'):
            return isMatch(pattern[1:], string[1:])
        
        else:
            return False
    

print(isMatch('A*A', 'AAA'))