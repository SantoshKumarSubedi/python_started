filename="pi_digits.txt"

"""reading whole file at once"""
with open(filename) as file_object:
    contents=file_object.read()
    print(contents)

"""reading one line at a time"""
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    print()

"""storing lines of file inlist"""

with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())
    print()

"""working with a file's content"""

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=""
for line in lines:
    pi_string+=line.rstrip()

print(pi_string)
print("Length of the string:"+str(len(pi_string)))
