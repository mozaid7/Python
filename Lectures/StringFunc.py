# str = "I am a coder"
# print(str.endswith("er"))

# print(str.capitalize())

# print(str.count("a"))

# marks =56

# if(marks>=90):
#     grade="A"
# elif(marks>=80 and marks<90):
#     grade = "B"
# elif(marks>=70 and marks<80):
#     grade = "C"
# else:
#     grade= "D"

# print("Grade of the student is:", grade)

#Greatest Number
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if(a>=b and a>=c):
   print("The greatest number is: ", a)
elif (b>=c and b>=d):
    print("Second is the largest", b)
elif (c>=d):
    print("Third is the largest", c)
else:
    print("Fourth is the largest", d)