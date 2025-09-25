# data types = this will tell which type of data type is the variable made of
# name = "tanmay"
# age = 19
# height = 12.99

# print(type(name))               #string (shows str in terminal)
# print(type(age))                #int
# print(type(height))             #float





#printing sum of 2 num
# a = 2
# b = 3
# sum = a ** b
# print(sum)      # * answer is 8

# single line comment

"""
multiline comments i think im using triple " before and after
"""


# ^ type conversion
# a = 2
# b = 4.25            # * natural conversion      (float is greater then int since it can store even more value then int so the compiler will prioritize float: when a+b)
# print(a + b)        #ans 6.25

# x = int("4")    # * this is now a string variable: before: x = "2"      after: x = int("2")  this method is called typecasting when the user forcefully changes the data type of a var.
# y = 4.25
# print(x + y)        # ? typecasting will only work if the data which we are trying to convert to a desired data type matches that desired data type's criteria for int = 0-9

# change = 3.14           #* was float
# print(type(change))         
# change = str(3.14)
# print(type(change))     #* now is string




# #^ input in python

# name = input("enter your name: ")
# print(f"hey this has been printed: {name}")
# #* or
# print("hey this is same but different: ", name)     #? its kinda like C

# #* whenever input takes any kind of input it converts into string automatically         to convert the input to the appropriate type u have to use typecast
# diff_name = input("enter any different name: ")
# age = int(input("enter you age: "))
# fav_decimal = float(input("enter your favourite float value: "))        # thse are the ways. how we convert the strings from the input.

# print("your given name: ", diff_name)
# print("your given age: ", age)
# print(f"your favourite decimal value: {fav_decimal}")




# #^ writing a program to input 2 numbers and print their sum
# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))
# print("this is the sum of those 2 given numbers : ", num1 + num2)

# #^ enter side of a square to print its area (area of a square = side * side or side^2)
# print("printing area of a square")
# side = float(input("enter one side of the square: "))
# print("area of the square is : ", side * side)      #* or we can do "side ** 2" this translates to 2 to the power of side

# #^ input 2 int numbers a and b   print True if a>= b if not print False
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# if a >= b:
#     print("True (because a is greater then b)")
# else:
#     print("False (because a is not greater then b)")
# #? this is how it was done in tutorial
# print(a >= b)   #& prints True if true and prints False if false statement




# #^strings       (stores a sequence of characters)
# str1 = "double quotes are used to define string usually but in python we can use even single quotes or even triple quotes"
# str2 = 'this is single quote'
# str3 = """this is triple quote""" 
# print(str1)
# print(str2)
# print(str3)


# #^ concatenation: joining 2 strings together
# str1 = "ganne ka "
# str2 = "juice"
# print(str1 + str2)

# #^ getting length of a string 
# str = input("enter some string: ")
# print(f"the length of your entered string : {len(str)}")      #* spaces are also counted in len()
# print(f"0th index of string: {str[0]}")

# #^ slicing
# slicing = "apple juice"
# print(slicing[0:5])     #* the starting "index is always included" when slicing but the "ending index in not included" when slicing
# #? [ :5] automatically take the starting index 
# #? [6: ]  automatically take the ending index

# #! negetive indexes this is a concept original from python      (these negetive indexes ONLY exists in slices)
# str = "apple"
# """
#  a  p  p  l  e
# -5 -4 -3 -2 -1 
# """
# print(str[-5: -2])



#^ types of strings 
str = "i am acting as a default string here"

# #* endswith() 
# print(str.endswith("ere"))      #? True if ends with given string
# print(str.endswith("er"))       #? False if doesnt end with given string

# #* capitalize()
# print(str.capitalize())         #? doesnt modify the original string
# print(str)
# str = str.capitalize()          #? for making permanent changes into the original string
# print(str)

#* replace(old, new)            #changing old value to new value
print(str.replace("a", "u"))
print(str.replace("acting", "not aloo bhujia"))