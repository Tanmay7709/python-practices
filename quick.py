# import sys

# n = int(sys.argv[1])   # Takes value from command line
# if 1 <= n <= 50:
#     print("Ok")
# else:
#     print("Out of range")


# nums = [10, 20, 30, 40, 50]

# # number = [0] * 5
# # for i in range(5):
# #     number[i] = int(input(f"Enter #{i+1}: "))

# # for j in range(5):
# #     print(f"#{j+1}: {number[j]}\t", end="") #* end="" doesnt let print trigger the \n when he's done
# # print() 
# average = sum(nums) / len(nums)
# print(f"average of nums: {average}")

# nums = []
# for i in range(6):
#     n = int(input(f"enter #{i+1}: "))
#     nums.append(n)

# duplicate = False
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):     #& start: 1 and end: 6  of j1
#         if nums[i] == nums[j]:
#             duplicate = True
#             break
#     if duplicate:
#         break

# if duplicate == True:
#     print("DUPLICATES")
# else:
#     print("ALL UNIQUE")



# nums = int(input("enter a value(1 to 50): "))
# if 1 <= nums <= 50:
#     print("Ok")
# else: 
#     print("Out of range")


# nums = int(input("Enter a number: "))
# digits_sum = 0

# while nums > 0:
#     digits_sum += nums % 10
#     nums //= 10
# print(f"Sum of given digits: {digits_sum}")




# n = int(input("enter how many fibonacci numbers you want: "))

# a, b = 0, 1
# print("Fibonacci series: ", end=" ")

# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# print()






# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a == b:
#     print("SAME identity")
# else:
#     print("DIFFERENT identity")




# num = input("enter any numbers to reverse: ")
# print("reversed numbers: ", end=" ")
# for i in range(-1, -len(num)-1, -1):
#     print(num[i], end=" ")
# print()

# for i in range(len(num)-1, -1, -1):
#     print(num[i], end=" ")
# print()                                   # both are working but i found the first one more convincing




# def sequential_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# numbers = [10, 20, 30, 40, 50]
# item = 30
# index = sequential_search(numbers, item)

# if index != -1:
#     print(f"Element found at index {index}")
# else:
#     print("Element not found")



# def mid_slice(str):
#     if len(str) < 2:
#         return ""
#     return str[:2] + str[-2:]

# # Examples
# print(mid_slice("General12"))  # Output: Ge12
# print(mid_slice("Ka"))         # Output: KaKa
# print(mid_slice("K"))          # Output: (empty string)




# my_string = "length without len_function"
# count = 0
# for char in my_string:
#     count += 1
# print(count)  # Output: 5




# s = input("Enter a string: ")
# letters = digits = 0

# for char in s:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1

# print("Letters:", letters)
# print("Digits:", digits)




# str = input("Enter a string: ")
# new_str = str[::2]
# print("modified string(removed odd indexes) : ", new_str)




# sentence = input("Enter a sentence: ")
# words = sentence.split()
# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# print("Word frequency:", freq)





# import string

# s = "/*Sachin is @Cricketer& kind person"
# clean_s = ''.join(char for char in s if char.isalnum() or char.isspace())
# print("Cleaned string:", clean_s)






# aTup = (10, 20, 30, 40, 50)
# revTup = aTup[::-1]
# print("Reversed tuple:", revTup)




# tup = (1, 2, 3)
# a, b, c = tup
# print(f"a = {a}, b = {b}, c = {c}")



# tup = (1, 2, 3)
# tup = tup + (4,)   # tuples are immutable, so we create a new one
# print("Updated tuple:", tup)



# tup = ('H', 'e', 'l', 'i', 'c', 'o', 'p', 't', 'e', 'r')
# str1 = ''.join(tup)
# print(str1)




# tup = (10, 20, 30, 40, 50, 60, 70)
# print("5th from front:", tup[4])
# print("5th from last:", tup[-5])




# tup = (10, 20, 30, 40, 50)
# print(30 in tup)   # True
# print(100 in tup)  # False




# s = {10, 20, 30, 40}
# if len(s) == 0:
#     raise KeyError("Set is empty")
# else:
#     element = s.pop()
#     print("Removed element:", element)
#     print("Remaining set:", s)





# s = {"apple", "banana", "cherry"}
# for item in s:
#     print(item)





# A = {1, 2, 3}
# B = {3, 4, 5}
# print("Union:", A | B)   # or A.union(B)



# A = {1, 2, 3}
# B = {2, 3, 4}
# print("Intersection:", A & B)   # or A.intersection(B)



# s = {10, 50, 30, 5, 100}
# print("Max:", max(s))
# print("Min:", min(s))



# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print("Difference (A-B):", A - B)
# print("Symmetric Difference:", A ^ B)




# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print("Union:", A | B)
# print("Intersection:", A & B)
# print("Difference A-B:", A - B)
# print("Difference B-A:", B - A)
# print("Symmetric Difference:", A ^ B)



# s1 = {1, 2, 3, 4}
# s2 = s1.copy()
# print("Original set:", s1)
# print("Shallow copy:", s2) 


# name = input("enter name: ")
# print(f"your entered name: {name}")


# string methods: 
hello = "hElu"
print(hello.capitalize())

# for i in range(10):
#     print(i + 1)

# range goes like this
# * stop  
# * start, stop
# * start, stop, step

# x = [2, 4, 5, 6, 7, 8, 9]
# for i in range(len(x)):
#     print(x[i])

# # dict
# x = {2, 3, 5, 6, 7}         # this is dictionary and dict is the word which is used more frequently
# y = {4, 6, 8, 4, 7, 3, 6, 4}
# z = {"key" : 4, "key2" : 7}         # * it has "key" = value
# for key in z:
#     print("key : ", z[key])     # * it willl give both key and value

# print(x)
# print(set(y))       # set will remove all the duplicate elements
# print(2 in x)
# print(90 in y)      # this will check 


def func(x , y):
    print("running", x , y)

func(4 , 6)
