#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existant_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#Catch exception:
#Attempt something
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["bgvrfukyj"])
# #Except to catch specific errors not just execute and miss the errors in the main code
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# #Use the error message to find out exact what key is causing the error
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# #Execute when try block successfully runs
# else:
#     content = file.read()
#     print(content)
# #Run no matter what
# finally:
#     # file.close()
#     # print("File was closed.")
##    Raise your own error. Use for unrealistic inputs (See bmi calc bellow)
#     raise TypeError("This is an error I made up")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)