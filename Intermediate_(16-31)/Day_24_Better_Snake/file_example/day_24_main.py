# # file = open("Hello.txt")
# with open("Hello.txt") as file:
#     contents = file.read()
#     print(contents)
#     # file.close()

with open("./Day_24_Better_Snake/file_example/Hello.txt", mode="a") as file:
    file.write("\nNew text")