print("Welcome to Notes Manager")

def add():
    title = input("Note Title: ")
    notes = input("Add Note:")

    with open('notes.txt', 'a') as f:
        f.write(title + "|" + notes +"\n")



def view():
     with open('notes.txt', 'r') as f:
       for line in f.readlines():
           data = line.rstrip()
           title, note = data.split("|")
           print("Title:", title +  "|"  + "Note:", note)
    

while True:
    mode = input("Would you like to ad a new note or view existing notes? (view, add), press q to quit"   ).lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Mode")
        continue
