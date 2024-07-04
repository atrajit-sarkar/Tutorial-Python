with open("handling_file/mytext.txt",) as somu:
    line=somu.readlines() #list output
    # line1=somu.readline()  #str output


l=[]
for i in line:
    i=i.split()
    l=l+i
l1=[]
for i in l:
    i=int(i)
    l1.append(i)


# print(l1)
def avg(nums):
    s=0
    for i in nums:
        s=s+i
    a=s/len(nums)
    return a
a=avg(l1)
# print(a)
with open("handling_file/write.txt","w") as f:
    f.writelines(f"The Average is : {a}")
print("Writing Successfull")