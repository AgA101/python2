class Operator:
    def __init__(self,name,x,y,r,f):
        self.name = name
        self.x = x
        self.y = y
        self.r = r
        self.f = f
obj_list = []
m = int(input())
k = 0
for obj in range(m):
    obj = Operator(str(input()),0,0,0,0)
    obj_list.append(obj)
    row = list(map(int, input().split()))
    obj_list[k].x = row[0]
    obj_list[k].y = row[1]
    obj_list[k].r = row[2]
    k += 1
g,h = map(int, input().split())

for j in range(m):
    if (obj_list[j].x - g) ** 2 + (obj_list[j].y - h) ** 2 <= obj_list[j].r ** 2:
        obj_list[j].f = 1

for p in range(m):
    for w in range(m):
        if obj_list[p].name == obj_list[w].name and p != w:
            obj_list[p].f += obj_list[w].f

            obj_list[w].name = ""
summ = 0
for e in range(m):
    if obj_list[e].name != "":
        summ += 1
print(summ)
for q in range(m):
    if obj_list[q].name != "":
        print(obj_list[q].name,obj_list[q].f)


