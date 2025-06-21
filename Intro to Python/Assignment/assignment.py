# # #Q1 Python program to sum the first n positive numbers
# choice = int(input("Enter the number till where to want sum:"))
# i=0
# sum=0
# while(i<=choice):
#     sum=sum+i
#     i=i+1
# print(sum)


#Q2 Python program to count occurence of substring in a given string
# Main_String = "cathatcathathat"
# Substring = "hat"
# count = Main_String.count(Substring)
# print(count)    


#Q3 Python program to count occurence of each word in given sentence
# string = input("Enter string:")
# word = input("Enter string:")
# count=string.lower().count(word)
# print(count)
# print(word)


#Q4 Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# s1 = "hello"
# s2 = "world"
# print("Single string is:",s1+s2)
# if len(s1) >=2:
#     s=s1[1]+s1[0]+s1[2:]
# if len(s2)>=2:
#         ss=s2[1]+s2[0]+s2[2:]
#         print(s+" ",ss,sep =" ")


#Q5 Write a Python program to add 'ing' at the end of a given string (length should be
#  at least 3). If the given string already ends with 'ing' then add 'ly' instead If the
#  string length of the given string is less than 3, leave it unchanged
# string = input("Enter string: ")
# if(len(string)>=3):
#     if(string[-3::1]=="ing"):
#         print(f"Already have ing hence:{string[:-3:1]+"ly"}")
#     else:
#         print(f"String is:{string+"ing"}")
# else:
#     print(f"String length less than 3 hence:{string}")


#Q6 Write a Python program to find the first appearance of the substring 'not' and
#  'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#  substring with 'good'. Return the resulting string
# str ="Nobody is 'not' said to be 'poor' by birth"
# for i in range(0,1):
#     i1=str.index('not')
#     i2=str.index('poor')
#     if(i==i1):
#         break
#     else:
#         print("Resulting string is: ",str[0:i1-1:]+"good"+str[i2+5::])


#Q7 Program to find Greatest Common Divisor of two numbers. For example, the
#  GCDof20 and 28 is 4 and the GCD of 98 and 56 is 14.
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# l=[]
# for i in range(2,num2//2):
#     if(num1%i==0 and num2%i==0):
#            l.append(i)
# print(max(l))


#Q8   Write a Python program to check whether a list contains a sublist.
# list = [1,2,3,4,5,6,7,8,9,10]
# match = False
# sub_list = [5,6,7]
# for i in range(len(list)-len(sub_list)+1):
#     if list[i:i+len(sub_list)] == sub_list:
#         match = True
#         break
# if match:
#     print("FOUND")
# else:
#     print("NOT FOUND")

#Q9  write a program to find the second smallest number from list
# numbers = [5,8,7,4,6,9]
# unique_numbers = sorted(set(numbers))   #set() remove duplicate
# second_smallest = unique_numbers[1]
# print("Second smallest:",second_smallest)


#Q10  Write a Python program to get unique values from a list.
# list = [1,2,3,4,5,6,7,8,1,5,4,2,5]
# unique_list = []
# for i in list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list) 

# # #Q11 Write a Python program to unzip a list of tuples into individual lists.
# zip_list = [('khush',20),('hello',25),('world',55)]
# #to unzip the list we use zip(*)
# name ,age =zip(*zip_list)
# name = list(name)
# age = list(age)
# print(name+age)

# # #Q12  Write a Python program to convert a list of tuples into a dictionary
# list = [('khush',21),('hello',25),('world',55)]
# dict = {}
# for key,value in list:
#     dict[key]=value
# print(dict)


# # #Q13  Write a Python program to sort a dictionary (ascending /descending) by value.
# dict = {'a':1,'b':2,'c':3}
# choice = int(input("ASCENDING OR DESCENDING? :(0/1))="))
# if choice==0:
#     print(sorted(dict.items()))
# elif choice==1:
#     print(sorted(dict.items(),reverse=True))
# else:
#     print("WRONG INPUT")


#Q14  Write a Python program to find the highest 3 values in a dictionary.
# dict = {1:'one',2:'two',3:'three',4:'four'}
# sorted_item = sorted(dict.items(),reverse=True)
# for key,value in sorted_item[:3]:   #slicing
#     print(f"{key}: {value}")    


#Q15  Given a number n, write a python program to make and print the list of Fibonacci series up to n.
# num = int(input("Enter the number: "))
# a=0
# b=1
# for i in range(0,num):
#     a,b=b,a+b
#     print(a)


# #Q16  Counting the frequencies in a list using a dictionary in Python.
# list = [14,15,14,1,5,4,6,5,1]
# # print(list.count(list[1]))
# for i in range(len(list)):
#     a = (list[i],list.count(list[i]))
#     print(set(a))


# #Q17  Write a python program using function to find the sum of odd series and even
# #  series
# #  Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
# #  Even series: 22/ 2! + 42/ 4! + 62/ 6!+

# # def factorial(n):
# #     res = 1
# #     for i in range(2,n+1):
# #         res = res*i
# #     return res
# # def odd_series(n):
# #     total = 0
# #     for i in range(1,n+1,2):
# #         total+= (i **2 )/factorial(i)
# #     return total
# # def even_series(n):
# #     total = 0
# #     for i in range(2,n+1,2):
# #         total+= (i **2 )/factorial(i)
# #     return total

# # n = int(input("enter the max value of n:"))
# # print(odd_series(n))
# # print(even_series(n))

# #Q18  Python Program to Find Factorial of Number Using Recursion
# # def factorial(num):
# #     if(num == 1 or num == 0):
# #         return 1
# #     return num * factorial(num-1)
# #a = factorial(5)
# #print(a)


#Q19. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# def unique_list():
#     num = int(input("Enter total number of elements: "))
#     l = []
#     for i in range(0,num):
#         a = int(input(f"Enter element {i}: "))
#         if(type(a)==int):
#             l.append(a)
#         else:
#             print("Invalid value")
#     new_list = []
#     for i in l:
#         if i not in new_list:
#             new_list.append(i)
#     print(new_list)


# # # unique_list()


# # #20. MINI PROJECT----> PASSWORD GENERATOR
# import random
# import string
# def password_generator():
#     try:
#         words = input("Enter the words for your password: ")
#         pass_str = ""
#         pass_str = pass_str+words
#         length = len(pass_str)
#         letters = string.ascii_letters
#         rem_words = 6-len(words)
#         if rem_words >0:
#             for i in range(rem_words):
#                 pass_str = pass_str + random.choice(letters)
#         l1 = []
#         l1.append(pass_str)
#         x = list(zip(*l1))
#         random.shuffle(x)
#         data = x
#         res = ''.join(tup[0] for tup in data)

#         pass_digit = ""
#         for i in range(3):
#             digits = string.digits
#             pass_digit = pass_digit+random.choice(digits)

#         pass_pun = ""
#         for i in range(2):
#             sp_symbol = string.punctuation
#             pass_pun = pass_pun + random.choice(sp_symbol)

#         r1 = res+pass_digit+pass_pun
#         r2 = res+pass_pun+pass_digit
#         result = random.choice([r1,r2])
#         if len(result)>=10:
#             print(f'''Your password is: {result}
#             !!!STRONG PASSWORD!!!
#           ....DO NOT SHARE....''')
#     except Exception as e:
#         return e
    
# password_generator()