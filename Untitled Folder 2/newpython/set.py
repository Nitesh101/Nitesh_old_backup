#!/usr/bin/python
"""
charset = set("A python tutorial")
dtype = type(charset)
print "type of charset",dtype


charset = set("perl","python","java")
dtype = type(charset)
print "type a chareset ",dtype


char = [3,9,1,2,23,2,3,4,5,5,6]
print list(set(char))



language = ("Perl","Pyton","Java")
listset = set(language)
print type(listset)
print "set is:",listset






tup1 = ("Python","Perl")
tup2 = ("Paris","Berlin","London")
cities = set((tup1,tup2))
print cities

"""


cities = ["Frankfurt","Basel","Freiburg"]
cities = set(cities)
print "Before adding values:\n",cities
cities.add("Strasbourg")
print cities












