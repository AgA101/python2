class Driver:
    def __init__(self,name,t):
        self.name = name
        self.t = t

obj_list = []
m,n = map(int, input().split())
k = 0
for obj in range(m):
    obj = Driver(str(input()),0)
    obj_list.append(obj)
    A = []
    row = list(map(int, input().split()))
    obj_list[k].t = sum(row)
    k += 1
minn = 100000
for j in range(m):
    if obj_list[j].t < minn:
        minn = obj_list[j].t
for h in range(m):
    if obj_list[h].t == minn:
        print(obj_list[h].name)
        break






