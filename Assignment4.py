##1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
##area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

class poly:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

class triangle(poly):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def get_area(self):
        s = (a + b + c)/2
        area=(s*(s-a)*(s-b)*(s-c))** 0.5

        return area
t = triangle(a,b,c)
print("area : {}".format(t.get_area()))

##1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
##the list of words that are longer than n.


def filter_long_words(n,string):
    word_len=[]
    txt=string.split(" ")
    for i in txt:
        if len(i)>n:
            word_len.append(i)
    return word_len


print(filter_long_words(4,"my name is tarun reddy"))




##Write a Python program using function concept that maps list of words into a list of integers
##representing the lengths of the corresponding words.
##Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
##Here 2,3 and 4 are the lengths of the words in the list.


def wordlengths(wordlist):
 return list(map(lambda x: len(x), wordlist))
wordlist = ["my", "best", "wishes", "for", "you"]
print ("word length is :" + str(wordlengths(wordlist)))

##2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
##it is a vowel, False otherwise.



def vowelCheck(Char):
    if (Char == "a" or Char == "A" or
            Char == "e" or Char == "E" or
            Char == "i" or Char == "I" or
            Char == "o" or Char == "O" or
            Char == "u" or Char == "U"):
        return "True"
    else:
        return "False"


print("Enter the string to check")
Char = input()

if vowelCheck(Char) == "True":
    print("The enterted character is Vowel")
else:
    print("The enterted character is not Vowel")

