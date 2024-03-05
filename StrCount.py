a="rounakjangid98$$@"
alphabet=digit=special=0
for i in range (0,len(a)):
    if(a[i].isalpha()):
        alphabet+=1
    elif(a[i].isdigit()):
        digit+=1
    else:
        special+=1

print(f"Alphabets are {alphabet}")
print(f"Digits are {digit}")
print(f"Special Symbols are {special}")