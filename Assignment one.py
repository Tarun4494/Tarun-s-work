#Assignment 1
#1.write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and
#and 3200(both included).The numbers obtained should be printed in a comma separated sequence on a single line.
n=[]
for x in range (2000,3200):
    if(x%7==0)&(x%5!=0):
        n.append(str(x))
print(" ".join(n))
#2.write a python program to accept the user's first and last name and then getting them printed in the reverse order with
# space between first name and last name.
fname=input("enter your first name")
lname=input("enter your last name")
print("how r u "+lname+"  "+fname)
#3.write a python program to find the volume of a sphere with diameter 12cm
#formula v=4/3 *pi*r**3
pi=3.1415
d=12.0
r=6.0
v=4.0/3.0*pi*r**3
print("volume of the sphere: ",v)