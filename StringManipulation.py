#"" String Manipulation in Python
"""name="python programming"
print(len(name))  # Output: 18
print(name.upper())  # Output: PYTHON PROGRAMMING
print(name.lower())  # Output: python programming
print(name[-1])  # Output: g
print(name[0:6])  # Output: python

for char in reversed(name):
    print(char,end='')  # Output: gnimmargorp nohtyp
print(name.strip())  # Output: python programming
print(name.replace("python", "java"))  # Output: java programming
print(name.split())  # Output: ['python', 'programming']
print("-".join(name))  # Output: p-y-t-h-o-n- -p-r-o-g-r-a-m-m-i-n-g
print(name.find("program"))  # Output: 7
print(name.count("o"))  # Output: 2
print(name.startswith("py"))  # Output: True
print(name.endswith("ing"))  # Output: True
print(name.isalpha())  # Output: False
print(name.isdigit())  # Output: False
print(name.capitalize())  # Output: Python programming
print(name.title())  # Output: Python Programming
print(name.swapcase())  # Output: PYTHON PROGRAMMING
print(name.index("gram"))  # Output: 10
print(name[::-1])  # Output: gnimmargorp nohtyp
print(name.center(30, '*'))  # Output: *******python programming******* 
print(name.ljust(25, '-'))  # Output: python programming-------
print(name.rjust(25, '-'))  # Output: -------python programming
print(name.partition(" "))  # Output: ('python', ' ', 'programming')
count=0
for i in name:
    if i in 'aeiou':
        count+=1
print(count)  # Output: 4"""
"""palindrome="madam"
if palindrome==palindrome[::-1]:
    print(f"{palindrome} is a palindrome")  # Output: madam is a palindrome
else:
    print(f"{palindrome} is not a palindrome")"""
#two pointer approach to check palindrome
"""s="madam"
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
if is_palindrome(s):
    print(f"{s} is a palindrome")  # Output: madam is a palindrome
else:
    print(f"{s} is not a palindrome")"""
#count frequency of each character in a string
s="apple"
for ch in s:
    print(ch,":",s.count(ch))

name="python"
result=""
for ch in name:
    if ch in "aeiou":
        result+="*"
    else:
        result+=ch
print(result)  # Output: pyth*n