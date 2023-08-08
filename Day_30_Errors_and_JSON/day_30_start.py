#FileNotFound
# with open("a_file.txt") as file:
#     file.read()
#Catch exception: try
try:
    file = open("a_file.txt")
except:
    print("There was an error")
#KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existant_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)