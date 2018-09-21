#!/usr/bin/python

v1 = 10.0
v2 = 10.0
idv1 = id(v1)
idv2 = id(v2)
print idv1,idv2


v1 = 20
v2 = 20
res = v1 is v2
print res

idv1 =id(v1)
idv2 =id(v2)
print idv1,idv2



v1,v2 = 50,35
small = v1 if v1 <v2 else v2
print small




cond = 'true'if True else 'false'
print cond
cond = 'false'if False else 'True'
print cond
