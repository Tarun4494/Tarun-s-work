#1.Create below pattern using nested for loop
num=int(input("enter number of rows: "))
for i in range(num):
   print("* "*(i+1)+"  "*(num-i-5))
for i in range(num-1):
    print("* "*(num-i-1)+"  "*(i+1))


##2.Write a python program to reverse a word after accepting the input from the user?
t=input("enter the word: ")
print (t[::-1])

