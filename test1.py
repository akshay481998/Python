class bank:

    def transactions(self):
        print("Total transaction value")

    def account_opening(self):
        print("This will show you your account opening status")

    def deposit(self):
        print("This will show you deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("This will show you all the transactions happened to icici through hdfc")

class icici(HDFC_bank):
    pass   #multilevel inheritance

i = icici()
i.account_opening()
i.deposit()
i.transactions()
i.hdfc_to_icici()