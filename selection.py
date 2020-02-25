list=[3,4,5,1,2,7,8]
l=len(list)-1
def selection(list):
    for i in range(l):
        min=i
        print(min)
        for j in range (i,l+1):
            if list[j]<list[min]:
                min=j
                print(min)
        list[min],list[i]=list[i],list[min]

selection(list)
print(list)