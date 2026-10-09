class Category:
    def __init__(self, name):
        self.ledger = []
        pass

    def deposit(self, amount, description):
        if not description:
            description = ''
        self.ledger.append({'amount': amount, 'description': description})

def create_spend_chart(categories):
    pass