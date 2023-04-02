# a1 = [4, 0, 1, -2, 3]
# a2 = [9, 3]
# a3 = [1, 2, 3, 4]

# def solution(a):
#     b = [0] * len(a)
#     if len(a) == 1:
#         return a
#     b[0] = 0 + a[0] + a[1]
#     b[len(a)-1] = a[len(a) - 2] + a[len(a) - 1] + 0
#     for i in range(1, len(a)-1):
#         b[i] = a[i-1] + a[i] + a[i+1]
#     return b

# print(solution(a1))
# print(solution(a2))
# print(solution(a3))
        
# def solution(s): 
#     curr_pal = 0
#     if len(s) == 0:
#         return ""       
#     if len(s) == 1: 
#         return s
#     for i in range(len(s)):
#         if is_palindrome(s[0:i+1]):
#             curr_pal = i+1

#     if curr_pal >= 2:
#         return solution(s[curr_pal:len(s)])
#     else:
#         return s


# def is_palindrome(str):
#     for i in range(len(str)//2):
#         low = i
#         high = len(str) - 1 - i
#         if str[low] == str[high]:
#             continue
#         else:
#             return False 
#     return True
        
# # print(is_palindrome('aaa'))
# print(solution('aa'))

# def updateBoard(board, click):
#     if board[click[0]][click[1]] == 'M':
#         board[click[0]][click[1]] = 'X'
#         return board
#     else:
#         return updateBoardHelper(board, click)

# def updateBoardHelper(board, click):
#     if is_click_valid(board, click):
#         checking = board[click[0]][click[1]]
#         checking_i = 0
#         # [3, 0]
#         if checking == 'E':
#             checking_i = is_mine(board, [click[0]-1, click[1]]) + \
#                         is_mine(board, [click[0]-1, click[1]+1]) + \
#                         is_mine(board, [click[0], click[1]+1]) + \
#                         is_mine(board, [click[0]+1, click[1]+1]) + \
#                         is_mine(board, [click[0]+1, click[1]]) + \
#                         is_mine(board, [click[0]+1, click[1]-1]) + \
#                         is_mine(board, [click[0], click[1]-1]) + \
#                         is_mine(board, [click[0]-1, click[1]-1])       
#             if checking_i == 0:
#                 board[click[0]][click[1]] = 'B'
#             else:
#                 board[click[0]][click[1]] = str(checking_i)
#         else:
#             return board

#         if board[click[0]][click[1]] == 'B':
#             # - [2, 0]
#             board = updateBoardHelper(board, [click[0]-1, click[1]])
#             # - [2, 1]
#             board = updateBoardHelper(board, [click[0]-1, click[1]+1])
#             # - [3, 1]
#             board = updateBoardHelper(board, [click[0], click[1]+1])
#             # - [4, 1]
#             board = updateBoardHelper(board, [click[0]+1, click[1]+1])
#             # - [4, 0]
#             board = updateBoardHelper(board, [click[0]+1, click[1]])
#             # - [4, -1]
#             board = updateBoardHelper(board, [click[0]+1, click[1]-1])
#             # - [3, -1]
#             board = updateBoardHelper(board, [click[0], click[1]-1])
#             # - [2, -1]
#             return updateBoardHelper(board, [click[0]-1, click[1]-1])
#         else:
#             return board
#     else:
#         return board

# def is_mine(board, click):
#     if is_click_valid(board, click):
#         if board[click[0]][click[1]] == 'M':
#             return 1
#     return 0

# def is_click_valid(board, click):
#     return click[0] >= 0 and click[0] < len(board) and click[1] >= 0 and click[1] < len(board[click[0]])



# print(updateBoard([
#     ["E","E","E","E","E"],
#     ["E","E","M","E","E"],
#     ["E","E","E","E","E"],
#     ["E","E","E","E","E"]],
#     [3,0]))
 
# # [["B","1","E","1","B"],
# # ["B","1","M","1","B"],
# # ["B","1","1","1","B"],
# # ["B","B","B","B","B"]]

# ["B","1","1","E","E"],
# ["B","1","M","1","E"],
# ["B","1","1","1","E"],
# ["B","B","B","B","E"]

# [1, 2, 3]

# [1]
# [1, 2]
# [1, 2, 3]

# [2]
# [2, 3]

# [3]

def solution(arr, k, s):
    num = 0
    for i in range(len(arr)):
        for j in range(i, k):
            if sum(arr[i:k+1]) == s:
                num += 1
    return num

print(solution([1, 0], 2, 1))
print(solution([1, 2, 4, -1, 6, 1], 3, 6))