"""cities=["vizag","delhi","mumbai","chennai","kolkata"]
cities.append("bangalore")
cities.insert(2,"hyderabad")
cities.remove("delhi")
cities.sort()
cities.reverse()
cities.pop()
print(cities)"""

#tuples are immutable
"""days=("mon","tue","wed","thu","fri","sat","sun")
print(days)
print(days.count("mon"))
print(days.index("fri"))   
print(days[1:3])
age=(25,30,35,40)
print("monday" in age)"""

"""friends=("ram","sham","rahim","karim")
print(friends)
print(friends[1])
print(friends[-1])
print(friends[0:2])
print(friends.count("ram"))
print(friends.index("karim"))
print("sham" in friends)
print(len(friends))
print(friends[::4])
print(friends[::-1])"""

#sets are unordered and unindexed
"""umbers={1,2,3,4,5,6}
numbers.add(7)#add single element
numbers.update([8,9,10])#add multiple elements
numbers.discard(89)#removes element if present else does nothing
numbers.remove(3)#removes element if present else raises error
numbers.pop()#removes and returns an arbitrary element
for i in numbers:
    print(i)
print(numbers)"""

#union,intersection,difference,symmetric difference
"""a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))#union means all elements from both sets
print(a.intersection(b))#common elements in both sets
print(a.difference(b))#elements in a but not in b
print(a.symmetric_difference(b))#elements in a or b but not in both"""
#Example
"""Marks={"predictive analysis:89","power bi:86","verbal ability:79","devops:80","automation testing:90","training in summer:51"}
for i in Marks:
    print(i)
Marks.add("data science:88")
Marks.remove("training in summer:51")
print(Marks)
Marks.update(["cloud computing:85","cyber security:87"])
print(Marks)
M={"predictive analysis:45","power bi:82","verbal ability:74","devops:21","automation testing:75","training in summer:51"}
print("common subjects:",M.intersection({"predictive analysis:89","power bi:86","verbal ability:79","devops:80","automation testing:90","training in summer:51"}))  
print("all subjects:",M.union({"predictive analysis:89","power bi:86","verbal ability:79","devops:80","automation testing:90","training in summer:51"}))
print("subjects in M but not in Marks:",M.difference({"predictive analysis:89","power bi:86","verbal ability:79","devops:80","automation testing:90","training in summer:51"}))
"""
#dictionaries are key-value pairs
"""student={"name":"john","age":21,"courses":["math","comp sci"]} 
print(student['name'])
print(student.get('age'))
student['age']=22
student['grade']='A'
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.update({'age':23,'grade':'A+'})
print(student)
student.pop('grade')
print(student)
del student['age']
print(student)
student.popitem()
print(student)
dict2=student.copy()
print(dict2)
print(len(student))"""
#Example    
"""students_info={'alice':20,'bob':22,'charlie':23}
students_marks={'alice':85,'bob':90,'charlie':95}
students_info.update(students_marks)
print(students_info)
students_marks.update(students_info)
print(students_marks)"""

#example
"""mobile_info={'brand':'samsung','model':'galaxy s21',"price":799,"stock":50}
print(mobile_info)
mobile_info['price']=15000
mobile_info['color']='black'
mobile_info.update({'stock':45,'warranty':'1 year','discount':10})    
print(mobile_info)
mobile_info.pop('model')
print(mobile_info)
print(mobile_info.keys())
print(mobile_info.values()) 
print(mobile_info.items())
print(len(mobile_info))
for key,value in mobile_info.items():
    print(f"{key}:{value}")
del mobile_info['discount']
print(mobile_info)
mobile_info.clear()
print(mobile_info)"""

#Reference and Object behavior
"""a=[1,2,3]
b=a
a.append(4)
print("a:",a)
print("b:",b)  """

"""a=10
b=a
b=20
print("a:",a)
print("b:",b)"""