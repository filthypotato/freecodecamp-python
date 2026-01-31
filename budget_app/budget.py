class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        lines = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            lines += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + lines + total

def create_spend_chart(categories):
    spent = []
    for cat in categories:
        cat_spent = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                cat_spent += -item["amount"]
        spent.append(cat_spent)

    total_spent = sum(spent)
    percents = []
    for s in spent:
        if total_spent == 0:
            percents.append(0)
        else:
            percents.append(int((s / total_spent) * 100) // 10 * 10)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for p in percents:
            if p >= level:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names) if names else 0

    for i in range(max_len):
        chart += "     "
        for n in names:
            if i < len(n):
                chart += n[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")
