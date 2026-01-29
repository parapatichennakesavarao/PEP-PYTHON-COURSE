"""print(True+True+False)
print("5"+"4")
print("5"*10)
def change(x):
    x+=10
a=5
change(a)
print(a)
"""
"""def update(first):
    first.append(10)
num=[1,2,3]
update(num)
print(num)"""

"""s={1,2,2,3,3}
print(len(s))
"""
"""try: 
    print("A")
    10/0
    print("B")
except:
    print("C")
print("D")"""
"""def test():
    try:
        return 1
    finally:
        return 2
print(test())"""
#move all zeors to the end of the list
"""nums=[0,1,0,3,12]
result=[]
zero_count=0
for num in nums:
    if num!=0:
        result.append(num)
    else:
        zero_count+=1
for i in range(zero_count):
    result.append(0)
print(result)"""
#palindrome using two pointer
"""s="racecar"
left=0
right=len(s)-1
is_palindrome=True
while left<right:
    if s[left]!=s[right]:
        is_palindrome=False
        break
    left+=1
    right-=1
print(is_palindrome)
"""
#longest word in a sentence
"""sentence="The quick brown fox jumped over the lazy dog"
words=sentence.split()
longest_word=""
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print(longest_word)"""
#highest sum in a list
"""nums=[1,2,3,4,5,6]
target=5
count=0
for num in nums:
    total=0
    for j in range(num,len(nums)):
        total+=nums[j]
        if total==target:
            count+=1
print(count)"""

"""nums=[2,7,11,15]

target=9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(nums[i],nums[j])
            break"""

#i want highest sum of 2 numbers in a list
"""nums=[3,5,1,8,2]
max1=0
max2=0
for num in nums:
    if num>max1:
        max2=max1
        max1=num
    elif num>max2:
        max2=num
print(max1+max2)"""

nums=[2,7,11,15 ]
target=9
left=0
right=len(nums)-1
while left<right:
    current_sum=nums[left]+nums[right]
    if current_sum==target:
        print(nums[left],nums[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1




