#algorithm for palindrome

# str = 'racecar'

# def isPalindrome(str):
#     startIndex = 0
#     endIndex = len(str) - 1

#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False
#     return True

# print(isPalindrome('nurses run'))    

def solution(inputString):
    startIndex = 0
    endIndex = len(inputString) - 1
    
    for x in inputString:
        if inputString[startIndex] != inputString[endIndex]:
            return False
            
    rev = inputString [::-1]
    print(rev)
    if inputString == rev:
        return True
    else:
        return False

print(solution('aaabaaaa'))