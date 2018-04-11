person={'name':'santosh','age':21,'color':'brown'}
print(person)

person['surname']='subedi'
person['balance']=2500;
print(person)

person['age']=20
person['bonus']='average'
print(person)

if person['bonus'].lower()=='low':
    increment=100
elif person['bonus'].lower()=="average":
    increment=150
else:
    increment=200

person['balance']+=increment

for key,value in person.items():
    print(str(key)+":"+str(value))

print(len(person))
