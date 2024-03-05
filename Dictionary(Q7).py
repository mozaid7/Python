thisdictionary = {
    "Name" : "Syed Mohd Zaid",
    "Section" : "S",
    "Registration Number" : "22BCON785",
    "Course" : "B.Tech CSE (AWS)",
    "Email" : "mohammedzee98@gmail.com"
}

print(thisdictionary)

thisdictionary["Duration"] = "2022-2026"
print(thisdictionary)

for x,y in thisdictionary.items():
    print(x,":", y)