num=int(input("Enter the number to be checked : "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number entered is palindrome")
else:
    print("Not a palindrome")