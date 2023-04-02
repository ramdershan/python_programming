# file  = open ('test.txt', mode = 'r')

# data = file.readline()

# print(data)

# file.close()

# with open('test.txt', mode = 'r') as file:
#     data = file.readline()

#     print(data)

# with open('newfile.txt', 'w') as file:
#     # file.write('This is a new file!')
#     file.writelines(['this is a new file', '\nthis is another line'])
try:
    with open('sample/newfile.txt', 'a') as file:
        # file.write('This is a new file!')
        file.writelines(['\nthis is a new file', '\nthis is another line'])
except FileNotFoundError as E:
    print('ERROR',E)