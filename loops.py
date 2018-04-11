usernames=[]
if usernames:
    for name in usernames:
        if name.lower()=="admin":
            print("Hello"+name.title()+",would you like to see a status report?")
        else:
            print("hello"+name.title()+",thank you for logging in again")
else:
    print("no username in the list")
