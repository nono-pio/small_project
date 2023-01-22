from dataHandle import DataHandle

db = DataHandle("first.db")

def printObj():
    items = db.getToDo(form="dict")
    for item in items:
        print(item)
        print("_"*20,"\n")
    print("\n")

printObj()