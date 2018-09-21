from collections import deque

dlst = deque()

print dlst,'\n'

dlst.append(2)
dlst.append(3)

print dlst,'\n'

dlst.appendleft(4)
dlst.appendleft(5)

print dlst,'\n'

print list(dlst)
