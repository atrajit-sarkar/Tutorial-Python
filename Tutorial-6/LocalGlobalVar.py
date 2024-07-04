a="Nobita"  #global variable
# s=0
def sum(*nums):
    s=0 #local variable
    for i in nums:
        s=s+i
    print(f"{a} did the sum.")
    return s

# print(sum(1,2,3,54))
# print(s+10)

