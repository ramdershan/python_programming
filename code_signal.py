# # # # def solution(numbers, left, right):
# # # #     results = []
# # # #     for i in range(len(numbers)):
# # # #         print(i)
# # # #         if numbers[i]%(i+1) == 0 and numbers[i]/(i+1) >= left and numbers[i]/(i+1) <= right:
# # # #             results.append(True)
# # # #         else:
# # # #             results.append(False)

# # # #     return results

# # # # print(solution([8,5,6,16,5], 1, 3))
        

# # # class HashMap(object):
# # #     def __init__(self):
# # #         self.dict = {}

# # #     def insert(self,x,y):
# # #         self.dict.update({x:y})

# # #     def get(self,x):
# # #         return self.dict[x]

# # #     def addToKey(self,x):
# # #         for k, v in self.dict.items():
# # #             new_key = k + x
# # #             self.dict.update({new_key : v})
# # #             self.dict.pop(k)

# # #     def addToValue(self,y):
# # #         for k, v in self.dict.items():
# # #             new_val = k + y
# # #             self.dict.update({k : new_val})
# # #             self.dict.pop(k)

# # # def solution(queryType, query):
# # #     hmap = HashMap()
    
# # #     for i in range(len(queryType)):
# # #         pass
    
# # #     pass

# # def solution(inputArray):
# #     max = -10000000   
# #     for i in range(len(inputArray)-1):
        
# #         product = inputArray[i] * inputArray[i+1]
# #         # print(product)

# #         if (product > max):
# #             max = product

# #     return max

# # a = [5, 1, 2, 3, 1, 4]
# # print(solution(a))

# def solution(sequence):
#     low = 0
#     for i in range(len(sequence)-1):
#         if sequence[i+1] <= sequence[i]:
#             low += 1
#         print(low)

#     if low > 1:
#         return False
#     else:
#         return True

# a = [1,2,1,2]
# print(solution(a))

# def solution(a):
#     count_arr = [0,0,0,0,0,0,0,0,0,0]
#     max = 0
#     max_int=[]
#     for i in range(len(a)):
#         for j in str(a[i]):
#             count_arr[int(j)] +=1
    
#     for i in range(10):
#         if count_arr[i] > max:
#             max = count_arr[i]
            
#     for i in range(10):
#         if max == count_arr[i]:
#             max_int.append(i)
    
#     return max_int

    

# print(solution([25,2,3,57,38,41]))

# def solution(arr):
#     for i in 

# def solution(sequence):
#     low = 0
#     for i in range(len(sequence)-1):
#         if sequence[i+1] <= sequence[i]:
#             low += 1
#         elif i <= (len(sequence) - 3) & sequence[i] == sequence[i+2]:
#             low += 1 
#         else:
#             continue
            
#     if low > 1:
#         return False
#     else:
#         return True

def solution(a):
    pass
    # reversing the matrix
    return 

def fizzBuzz(n: int) -> list[str]:
        l = []
        for i in range(1, n+1):
            if i%3 == 0 & i%5 == 0:
                l.append('FizzBuzz')
            elif i%3 == 0:
                l.append('Fizz')
            elif i%5 == 0:
                l.append('Buzz')
            else: 
                l.append(str(i))
        return l
    

print(fizzBuzz(3))

