with open("DefaultSop.txt") as sop:
    default_sop=sop.readlines()

# print(str_sop)

def listTostr(list):
    s=""
    for i in list:
        s=s+i
    
    return s
default_sop=listTostr(default_sop)
# print(default_sop)
with open("body.txt") as body:
    default_body=body.readlines()
default_body=listTostr(default_body)

def MassMail(designation,my_name="Atrajit Sarkar",instituteFrom="IITD",instituteTo="IIT Delhi",prof_name="Dr.Biplab Basak",sop=default_sop,body=default_body,interestTopics="Knot Theory, Algebraic Topology"):
    #Customized body of the mail:
    str=f'''Respected {designation}, {prof_name},
    I am {my_name},from {instituteFrom} wanted to apply for Phd in Mathematics in your institute {instituteTo}. I have interest in {interestTopics}.

SOP:
    {default_sop}


    
    '''
    return str

with open("composedmail.txt","w") as mail:
    mail.writelines(MassMail("sir","Abhishek Yadav"))
