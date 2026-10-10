class Category:
    def __init__(self, name):
        self.ledger = []
        pass

    def deposit(self, amount, description):
        if not description:
            description = ''
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description):
        neg_amount = amount * -1
        self.ledger.append(neg_amount)
        if self.withdraw:
            return True
        else:
            return False

def create_spend_chart(categories):
    pass