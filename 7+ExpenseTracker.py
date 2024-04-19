class Expense:
    def __init__(self, category, amount, description, month):
        self.category = category
        self.amount = amount
        self.description = description
        self.month = month

    def __str__(self):
        return f"{self.category}, {self.amount}, {self.description}, {self.month} "

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.actions = []
        self.sum = 0
        self.report = []

    def add_expense(self):
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        try: 
            amount = int(amount)
        except:
            print("Enter integer value for amount")
            amount = input("Enter amount: ")

        description = input("Enter description: ")
        month = input("Enter month: ")


        expense = Expense(category, amount, description, month)
        self.expenses.append(expense)
    
    def view_expenses_list(self):
        for i in self.expenses:
            print(i)

    def sum_of_expenses(self):
        category = input("Enter category: ")
        for expens in self.expenses:
            if expens.category == category:
                self.sum += expens.amount
        print(f"the sum of {category} is {self.sum}")


    def reports(self):
        res = ""
        month = input("Enter month: ")
        for expens in self.expenses:
            if expens.month == month:
                res+=str(expens)+"\n"
                print(expens)
        self.report.append(res)
        

    def save_reports(self):
        with open("expense.txt", "w") as file:
            for rep in self.report:
                file.write(rep + "\n")

        

    def start(self):
        self.actions = ["Add expens - 1", "View expenses list - 2", "Sum of expenses list - 3", "Reports - 4", "Save reports - 5", "quit - 6"]
        while True:
            for action in self.actions:
                print(action)

            action = input("Choose the action you want: ")
            if action == "1":
                self.add_expense()
            elif action == "2":
                self.view_expenses_list()
            elif action == "3":
                self.sum_of_expenses()
            elif action == "4":
                self.reports()
            elif action == "5":
                self.save_reports()
            elif action == "6":
                break
            else:
                print("Invalid action")            



expense = ExpenseTracker()
expense.start()





















