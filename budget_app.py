# project: Budget App
"""this project is a budget app that allows users to create different 
 budget categories, deposit and withdraw funds, transfer money between 
 categories, and visualize spending through a chart."""

class Category:
    def __init__(self, name):
        #name of the budget category
        self.name = name
        #ledger is a list that store money and withdraw
        self.ledger= []

    def deposit(self, amount, description=""):
        # store the money as a positive number
        self.ledger.append({"amount": amount,"description": description})

    def withdraw(self,amount, description=""):
        #withdraw ,Store as a negative number
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,"description": description})
            return True
        return False

    def get_balance(self):
        # adds up every amount in ledger
        total =0
        for item in self.ledger:
            total += item["amount"]
        return total

    #account transfer from one category to other
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # name centered in 30 characters, padded with '*'
        output = self.name.center(30, "*") + "\n"

        # one line per ledger item and the amount r aligned in 7 spaces with 2 decimal
        for item in self.ledger:
            desc =item["description"][:23].ljust(23)
            amt =f"{item['amount']:.2f}".rjust(7)
            output += f"{desc}{amt}\n"

        # last line shows the total balance
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    #1-calculate how much was spent per category
    spending= []
    for cat in categories:
        spent = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spending.append(spent)

    # total amount
    total_spent= sum(spending)

    # convert each spending amount to a percentage,
    percentages = []
    for s in spending:
        if total_spent >0:
            percent= int((s /total_spent) *100)
            rounded =(percent//10) *10
            percentages.append(rounded)
        else:
            percentages.append(0)

    chart ="Percentage spent by category\n"      #title

    #bars from 100 down to 0
    for level in range(100,-1,-10):
        chart += str(level).rjust(3)+ "| "
        for pct in percentages:
            if pct >= level:
                chart += "o  "
            else:
                chart+= "   "
        chart+= "\n"

    # horizontal line under the bars
    dash_count = 3*len(categories) +1
    chart +=  "    " + "-" * dash_count +"\n"

    #category names
    longest = 0
    for category in categories:
        if len(category.name) > longest:
            longest = len(category.name)
 
    for i in range(longest):
        chart += "    "         # 4 leading spaces
        for category in categories:
            if i < len(category.name):
                chart += " " + category.name[i] + " "
            else:
                chart += "   "
        chart += " " 
        if i < longest - 1:
            chart += "\n"
 
    return chart

food =Category('Food')
food.deposit(1000,'deposit')
food.withdraw(10.15,'groceries' )
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing =  Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)
print(create_spend_chart([food,clothing]))

