##1. Write a function to compute 5/0 and use try/except to catch the exceptions.
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")
##2.2. Implement a Python program to generate all sentences where subject is in
##["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
##["Baseball","cricket"].
subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)