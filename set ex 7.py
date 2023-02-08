list=[]
for i in range(0,5):
    list.append(i)
    list.append(4)
    list.append(5)
print("created list which contain duplicate list:",list)
X=set(list)
print("after creating set remove duplicate:",X)
