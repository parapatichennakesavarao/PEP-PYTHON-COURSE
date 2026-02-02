#(.)->any One character,example:c.t
#(^)->starts of String,example:"hello World" ^hello
#($)->ends of String,example:"hello World" World$
#(*)->zero or more times,example:ab*e->ae,abe,abbe,abbbe
#(+)->one or more times,example:ab+e->abe,abbe,abbbe but not ae
#(?) ->zero or one time,example:ab?e->ae,abe but not
#([])->Character set,example:a[bcd]e->abe,ace,ade
#(0-9)->any digit from 0 to 9,example:a[0-9]e->a0e,a1e,a2e...a9e
#(a-z)->any lowercase letter from a to z,example:a[a-z]e
#(A-Z)->any uppercase letter from A to Z,example:a[A-Z]e
#(A-Za-z)->any letter,example:a[A-Za-z]e
#(\d)->any digit,example:\d\d\d->123,456
#(\D)->any non-digit,example:\D\D\D->abc,@#
#(\w)->any word character(a-z,A-Z,0-9,_),example:\w\w\w->abc,ab1,a_2
#(\W)->any non-word character,example:\W\W\W->@#
#(\s)->any whitespace character(space,tab,newline),example:\s\s\s->"   ","\t\t\t"
#(\S)->any non-whitespace character,example:\S\S\S->abc,123,@#$
#({})->exactly n times,example:a{3}e->aaae
#({n,})->at least n times,example:a{2,}e->aae,aaae,aaaae
#({n,m})->between n and m times,example:a{2,4}e->aae,aaae,aaaae
#( | )->either or,example:cat|dog->cat,dog
#(())->grouping,example:(ab)+e->abe,abbe,abbbe
#escape character(\),example:\.->.,\*->*
import re
"""#example of dot(.)
text="cat cot cut"
result=re.findall("c.t",text)
print(result)  #['cat', 'cot', 'cut']
#example of starts with(^)
text2="hello World"
result2=(bool(re.search("^hello",text2)))
result3=(bool(re.search("^World",text2)))
print(result2)  #['hello']
print(result3)  #[]
#example of ends with($)
text2="hello World"
result2=(bool(re.search("hello$",text2)))
result3=(bool(re.search("World$",text2)))
print(result2)  #['hello']
print(result3)  #[]
#example of star(*) is zero or more times
text3="helloooo"
result4=re.findall("lo*",text3)
print(result4)  #['loooo']
#example of plus(+) is one or more times
text4="helloooo"
result5=re.findall("lo+",text4)
print(result5)  #['loooo']
#example of question mark(?) is zero or one time
text5="color colour"
result6=re.findall("colour?",text5)
print(result6)  #['color', 'colour']
#example of character set([]) is a set of characters
text6="apple ball cat dog"
result7=re.findall("[abc]",text6)
print(result7)  #['a', 'b', 'a', 'c', 'a']
#example of range(0-9) is any digit from 0 to 9
text7="My age is 30"
result8=re.findall("[0-9]",text7)
print(result8)  #['3', '0']
#example of range(a-z) is any lowercase letter from a to z
text8="My age is 30"
result9=re.findall("[a-z]",text8)
print(result9)  #['a', 'g', 'e', 'i', 's'] 
#example 2
text9="HelloWorld"
result10=re.findall("[a-z]",text9)
print(result10)  #['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
#example of range(A-Z) is any uppercase letter from A to Z
text10="HelloWorld"
result11=re.findall("[A-Z]",text10)
print(result11)  #['H', 'W']
#example of range(A-Za-z) is any letter from A to Z or a to z
text11="HelloWorld123"
result12=re.findall("[A-Za-z]",text11)
print(result12)  #['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
#example of \d is any digit
text12="My phone number is 123-456-7890"
result13=re.findall("\d\d\d",text12)
print(result13)  #['123', '456', '789']
#example of \D is any non-digit
text13="My phone number is 123-456-7890"
result14=re.findall("\D\D\D",text13)
print(result14)  #['My ', 'pho', 'num', 'ber', 'is']
#example of \w is any word character(a-z,A-Z,0-9,_)
text14="User_123!"
result15=re.findall("\w\w\w",text14)
print(result15)  #['Use', 'r_1', '23']
#example of \W is any non-word character
text15="User_@!*#123!"
result16=re.findall("\W\W",text15)
print(result16)  #['!']
#example of \s is any whitespace character(space,tab,newline)
text16="Hello \t World"
result17=re.findall("\s\s",text16)
print(result17)  #[' ']
#example of \S is any non-whitespace character
text17="Hello \t World"
result18=re.findall("\S\S\S",text17)
print(result18)  #['Hel', 'loW', 'orl']
#example of {} is exactly n times
text18="phone: 9885067525"
result19=re.findall("\d{10}",text18)
print(result19)  #['9885067525']
#example of {n,} is at least n times
text19="ae aae aaae aaaaae"
result20=re.findall("a{2,}e",text19)
print(result20)  #['aae', 'aaae', 'aaaae']
#example of {n,m}
text20="ae aae aaae aaaaae aaaaaaae"
result21=re.findall("a{2,4}e",text20)
print(result21)  #['aae', 'aaae', 'aaaae']
#example of (|) is either or
text21="I have a cat and a dog"
result22=re.findall("cat|dog",text21)
print(result22)  #['cat', 'dog']
#example of (()) is grouping
text22="abab ab"
result23=re.findall("(ab)+",text22)
print(result23)  #['ab', 'ab']"""

#Q1 write a regex pattern of validate 10 digit phone number
"""number=int(input("Enter the 10 digits Phone number: "))
pattern=re.findall("[0-9]{10}",str(number))
if pattern:
    print("Valid Phone Number: ",pattern[0])
else:
    print("Invalid Phone Number")

#OR
mobile=input("Enter the 10 digits Phone number: ")
pattern=r"^[0-9]{10}$"
if re.match(pattern,mobile):
    print("Valid Phone Number: ",mobile)
else:
    print("Invalid Phone Number")"""

#Q2  wite a sentence contact me at text@gmail.com or admin@yahoo.in 
"""email_input=input("Enter the Email ID: ")
email_pattren=r"[\w.-]+@[\w.-]+\.[a-z]"
if re.match(email_pattren,email_input):
    print("Valid Email ID: ",email_input)
else:
    print("Invalid Email ID")"""
#Exrtract all numbers from the given string
"""Text="Object 123 price45 Quantity 67"
find=re.findall("\d+",Text)
print("Extracted Numbers: ",find)"""  #['123', '45', '67']

#Q3 Validate a password which contains at least one uppercase letter, one lowercase letter, one digit, one special character and minimum length of 8 characters
"""password=input("Enter the password: ")
pattern=r"^[A-Za-z\d@#$%^&+=]{8,}$"
if re.match(pattern,password):
    print("Valid Password",password)
else:
    print("Invalid Password")"""
"""
PAN=input("Enter the pan number: ")
pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]$" 
if re.match(pattern,PAN):
    print("Valid PAN Number: ",PAN)
else:
    print("Invalid PAN Number")"""


IP_Adress=input("Enter the IP Address: ")
pattern=r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
if re.match(pattern,IP_Adress):
    print("Valid IP Address: ",IP_Adress)
else:

    print("Invalid IP Address")