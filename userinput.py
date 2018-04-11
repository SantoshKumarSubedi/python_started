flag='y'
voters=[]
while flag.lower()=='y':

    name=input("Enter name:")
    age=input("Enter age:")
    age=int(age)


    if age>=10:
        print(name+",you are eligible to vote")
        new_voter={name:{'age':age}}
        voters.append(new_voter)
    else:
        print(name+",you are not eligible to vote")
    print('list of voter up to now')
    for n in voters:
        for name,value in n.items():
            print(name)
            for valu in value.values():
                print("\tage:"+str(valu))
    flag=input("do you want to enter a new value?(Y/N)")
