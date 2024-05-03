import os

# if not os.path.exists("tukun"):
#     os.mkdir("tukun")    #mkdir:= make directory(folder)

# with open(r"tukun\main.py","w") as fuck:   #"w": write, r= raw string
#     fuck.write("")       # "":= empty string

N=int(input("Enter the number of files you want to make: "))

for i in range(3,N+1):
    if not os.path.exists(f"Tutorial-{i}"):
        os.mkdir(f"Tutorial-{i}")
        with open(rf"Tutorial-{i}\main.py","w") as fuck:
            fuck.write("")
