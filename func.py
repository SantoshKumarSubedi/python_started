def name_s(firstname,lastname,middlename=''):
    if middlename:
        fullname={'first':firstname,'middle':middlename,'last':lastname}
    else:
        fullname={'first':firstname,'last':lastname}
    return fullname
flag='y'
lis=[]
while flag.lower()=='y':

    first=input("enter first name")
    middle=input("enter second name")
    last=input("enter last name")
    sant=name_s(first,last,middle)
    lis.append(sant)
    for li in lis:
        for key,value in li.items():
            print('key:'+key+''+'value:'+value)
            print()
    flag=input("do you want any other record(Y/N)?")
