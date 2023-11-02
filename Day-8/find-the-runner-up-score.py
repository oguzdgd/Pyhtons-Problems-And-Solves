if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
list=[]
for i in arr:
    list.append(i)

list.sort()
mxm=max(list)
while list.count(mxm)>0:
    list.remove(mxm)

print(max(list))