#!/usr/bin/python3
from random import shuffle
from copy import deepcopy
from datetime import datetime as dt
s = dt.now()
l = []
for i in range(int(input())):
    l.append(i)
a = deepcopy(l)
shuffle(l)
while a!=l:
    shuffle(l)
print("Dumb Sort finished in ", (dt.now()-s))