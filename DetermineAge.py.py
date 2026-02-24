Age = int(input("Input Age: "))

Adult = Age > 17
Minor = Age < 17

if(Age > 17):
    print("Adult")
elif(Age < 17):
    print("Minor")