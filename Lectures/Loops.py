#--> WHILE Statement
# nums = (1,4,9,16,25,36,49,64,81,100)
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

#--> BREAK Statement
# nums = (1,4,9,16,25,36,49,64,81,100)
# val = int(input("Enter value to search: "))
# i = 0
# while i < len(nums):
#     if(nums[i]==val):
#         print("FOUND at index :", i)
#         break
#     else:
#         print("Finding...")
#     i += 1 

#--> CONTINUE Statement
# i = 0
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue #Skip Even numbers
#     print(i)
#     i += 1

#--> FOR Loop
# nums = (1,4,9,16,25,36,49,64,81,100)
# for val in nums:
#     print(val)

# nums = (1,4,9,16,25,36,49,64,81,100)
# for val in nums:
#     print(val)
# else:
#     print("END")

#--> RANGE Function
# nums = (1,4,9,16,25,36,49,64,81,100)
# for i in range(2,6):
#     print(nums[i])

#--> PASS Statement
# for i in range(5):
#     pass     #used when we want to leave the loop empty


#--> Factorial Question
# n = 6
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("The factorial is", fact)