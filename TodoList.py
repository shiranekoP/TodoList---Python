# Todo List Program - Noted *terminal app
# Developer : Pisit Sriamonkitkul - 10/16/2018

# Class & Function
class todoList:
    def __init__(self, list = None):
        if list:
            self.list = [list]
        else:
            self.list = []

    def getList(self):
        return self.list

    def addList(self, item):
        self.list.append(item)

    def getLen(self):
        if self.list == []:
            return 0
        else:   
            return len(self.list)

    def __str__(self):
        str = '-----------------------------------------------\n'
        for item in self.list:
            if(item == None):
                break
            str = str + item.__str__() + '\n'
        str = str + '-----------------------------------------------'
        return str

class todo:
    def __init__(self, id, detail = None, date = None, state = 'undone'):
        self.id = id
        self.state = 'Undone'
        if detail:
            self.detail = detail
        else:
            self.detail = "No Data"
        if date:
            self.date = date
        else:
            self.date = "No Data"

    def __str__(self):
        return "ID "+ str(self.getID()) +" :: " + str(self.getDetail()) +" :: " + str(self.getDate()) + " :: " + str(self.getState())

    def setID(self, id):
        self.id = id

    def setState(self, state):
        self.state = state

    def setDetail(self, detail):
        self.detail = detail

    def setDate(self, date):
        self.date = date

    def getID(self):
        return self.id

    def getState(self):
        return self.state

    def getDetail(self):
        return self.detail

    def getDate(self):
        return self.date

def commandControl(command, list, id):
    if command.upper().lower() == "/help":              # /help command
        print("-----------------------------------------------\n")
        print("/help            call a help command \n")
        print("/add             add a task to todo list\n")
        print("/done            check a task if it has been done\n")
        print("/display         display all undone tasks\n")
        print("/display_all     display all registered tasks\n")
        print("-----------------------------------------------")

    elif command.upper().lower() == "/display":         # /display display all undone tasks
        print("-----------------------------------------------\n")
        for i in list.getList():
            if i.getState() == "Undone":
                print(str(i) + "\n")
        print("-----------------------------------------------\n")

    elif command.upper().lower() == "/display_all":     # /display_all 
        print(list)

    elif command.upper().lower() == "/done":            # /done
        while True:
            try:
                inputID = int(input("Select ID: "))
                break
            except ValueError:
                print("Invailed ID. Must be number")
        if inputID > list.getLen() - 1:     #empty list = -1
            print("Entered ID doesn't exist")
        else:
            print("Update state of ID "+ str(inputID))
            list.list[inputID].setState("Done")

    elif command.upper().lower() == "/add":
        while True:
            inputDetail = str(input("Enter task detail (Up to 50 Character): "))
            if inputDetail == '':
                print("Task detail need to be filled")
                continue
            if len(inputDetail) > 50:
                print("Detail length must be lower than 50 character")
                continue
            break

        inputDate = str(input("Enter date (can empty): "))
        todoObj = todo(id, inputDetail,inputDate)
        list.addList(todoObj)

    else:
        print("Error Command !")


# Main
print("Welcome to Todo list program. Types /help for more command")
list = todoList()
id = 0
while True:
    command = str(input("Select Command: "))
    commandControl(command,list,id)
    if command.upper().lower() == "/add":
        id += 1
    print("\n")
