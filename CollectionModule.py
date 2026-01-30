from collections import Counter
#counting the occurrences of elements in a list
Fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'apple']
fruit_counter = Counter(Fruits)
print(fruit_counter)
#counting the occurrences of characters in a string
Text="Hello"
count=Counter(Text)
print(count)

Sentence="Python is easy and python is poweful"
Sentense_counter=Counter(Sentence.lower().split())
print(Sentense_counter)

numbers=[1,2,3,4,5,1,2,3,1,2,1]
number_counter=Counter(numbers)
print(number_counter)