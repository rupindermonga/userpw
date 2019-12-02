# Create login/ pwd and login with existing login/ pwd


db = {}

def newuser():
    pr = "desired loginid: "
    while True:
        username = input(pr)
        if username in db:
            pr = "username taken, try another: "
            continue
        else:
            break
    pwd = input('password: ')
    db[username] = pwd

def olduser():
    username = input('login: ')
    pwd = input('password: ')
    passwd = db.get(username)
    if passwd == pwd:
        print("Welcome back, ", username)
    else:
        print("Please check username/ password")

CMDs = {'n': newuser, 'e': olduser}

def showmenu():
    pr = '''
    (N)ew User
    (E)xisting User
    (Q)uit

    Enter choice: '''

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print("\nYou picked: [%s]" % choice)
            if choice not in 'neq':
                print("Invalid choice, try again")
            else:
                break
        
        if choice == "q":
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()