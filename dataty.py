#frozenset datatype
# a=frozenset({1,2,3,4,5,6})
# b=frozenset({4,5,6,7,8,9})
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.isdisjoint(b))
# print(a.issuperset(b))
# print(a.issubset(b))
# o/p-:
# frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})
# frozenset({4, 5, 6})
# frozenset({1, 2, 3})
# frozenset({1, 2, 3, 7, 8, 9})
# False
# False
# False

#list datatype
# l1=[10,20,30,40]
# l2=["python","java",10,10.3]
# print(l1)
# print(l2)
# print(l1.append(40))
# print(l1.extend(l2))
# print(l1.insert(2,50))
# print(l1.pop())
# print(l1.index(30))
# print(l1.count(10))
# print(l1.clear())
# o/p-:
# [10, 20, 30, 40]
# ['python', 'java', 10, 10.3]
# None
# None
# None
# 10.3
# 3
# 2
# None

#set datatype 
# s1={10,20,30}
# print(s1)
# s1.add(40)
# print(s1)
# s1.update([40,50,60])
# print(s1)
# s1.remove(30)
# print(s1)
# s1.discard(40)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)
# s2=s1.copy()
# print(s2)
# o/p-:
# {10, 20, 30}
# {40, 10, 20, 30}
# {40, 10, 50, 20, 60, 30}
# {40, 10, 50, 20, 60}
# {10, 50, 20, 60}
# {50, 20, 60}
# set()
# set()

#Method of set for more than to set
# a={1,2,3,4,5,6}
# b={4,5,6,7,8,9}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.intersection_update(b))
# print(a.difference_update(b))
# print(a.symmetric_difference_update(b))
# print(a.isdisjoint(b))
# print(a.issuperset(b))
# print(a.issubset(b))
# o/p-:
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# {4, 5, 6}
# {1, 2, 3}
# {1, 2, 3, 7, 8, 9}
# None
# None
# None
# False
# True
# True

#dictonery datatype
a={'a':10,'b':20,'c':30}
b={'x':40,'y':50,'z':60}
print(a,b)
print(type(a))
print(type(b))
