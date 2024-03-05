def findLargest(x,y,z):
    if x > y and x > z:
        
        
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

thislist = [num1, num2, num3]
largestNumber = 0
for x in thislist:
    if(largestNumber >= x):
        largestNumber = x

print(largestNumber)