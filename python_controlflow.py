http_stat = 200

####Python version 3.10
# match http_stat:
#     case 200 | 201:
#         print('success')
#     case 400:
#         print('Not Found')
#     case 500 | 501:
#         print('server error')
#     case _:
#         print('unknown')

likes = ['choco', 'banana', 'rice']

# for item in likes:
#     print('i like', item)

for idx, item in enumerate(likes):
    print(idx, item)

count = 0

while count < len(likes):
    print(likes[count])
    count+=1

#break, continue, pass